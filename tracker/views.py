from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login
from allauth.account.views import LoginView
from .forms import CustomLoginForm
from .models import Transaction
from .forms import TransactionForm
import openpyxl
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm

@login_required
def main(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
    else:
        form = TransactionForm()

   
   

    # Получаем транзакции пользователя
    transactions = Transaction.objects.filter(user=request.user)
    
    
    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense  # Баланс = доходы - расходы
    
    
    recommendations = RecommendationEngine(balance)

    return render(request, 'main.html', {
        'form': form,
        'transactions': transactions,
        'balance': balance,
        'recommendations': recommendations
    })

    
class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(self.get_success_url())
    
    



def export_transactions(request):
    # Создаем новую рабочую книгу Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Создаем заголовки для таблицы
    ws.append(['Name', 'Amount', 'Category', 'Transaction Type', 'Created At'])

    # Получаем все транзакции
    transactions = Transaction.objects.all()

    # Добавляем строки для каждой транзакции
    for transaction in transactions:
        ws.append([transaction.name, transaction.amount, transaction.category, transaction.get_transaction_type_display()])

    # Создаем HTTP-ответ с Excel-файлом
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="transactions.xlsx"'
    wb.save(response)
    return response

@login_required


def export_transactions_pdf(request):
    # Создаем HTTP-ответ для PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'

    # Создаем объект canvas для генерации PDF
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)

    # Заголовки для таблицы
    p.drawString(100, 750, "Name")
    p.drawString(200, 750, "Amount")
    p.drawString(300, 750, "Category")
    p.drawString(400, 750, "Transaction Type")
    p.drawString(500, 750, "Created At")

    # Получаем все транзакции
    transactions = Transaction.objects.all()
    y_position = 730

    # Добавляем строки для каждой транзакции
    for transaction in transactions:
        p.drawString(100, y_position, transaction.name)
        p.drawString(200, y_position, str(transaction.amount))
        p.drawString(300, y_position, transaction.category)
        p.drawString(400, y_position, transaction.get_transaction_type_display())
        p.drawString(500, y_position, str(transaction.created_at))

        y_position -= 20

    # Сохраняем PDF
    p.showPage()
    p.save()
    return response




def RecommendationEngine(balance):
    recommendations = []
    
    if balance < 0:
        recommendations.append("Your balance is negative. Try to cut down on expenses.")
    elif balance == 0:
        recommendations.append("You have no funds. Consider saving for future expenses.")
    elif 0 < balance <= 100:
        recommendations.append("Your balance is low. Try reducing spending in categories like shopping and entertainment.")
    elif 100 < balance <= 500:
        recommendations.append("Your balance is healthy. Consider saving some money for future needs.")
    elif balance > 500:
        recommendations.append("You have a good balance! Consider investing or saving more for future opportunities.")
    
    return recommendations