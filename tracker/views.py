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
from django.contrib import messages

@login_required
def main(request):
    
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  
            transaction.save()
            messages.success(request, "Транзакция успешно сохранена!")
            return redirect('/') 
        else:
            messages.error(request, "Ошибка: проверьте введенные данные.")
    else:
        form = TransactionForm()

   
    transactions = Transaction.objects.filter(user=request.user)

    
    total_income = transactions.filter(transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense  # Баланс = доходы - расходы


    recommendations = RecommendationEngine(balance).get_recommendations()

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
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Transactions"

    
    ws.append(['Name', 'Amount', 'Category', 'Transaction Type', 'Created At'])

    
    transactions = Transaction.objects.all()

    
    for transaction in transactions:
        ws.append([transaction.name, transaction.amount, transaction.category, transaction.get_transaction_type_display()])

   
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="transactions.xlsx"'
    wb.save(response)
    return response

@login_required


def export_transactions_pdf(request):
   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'

    
    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)

    
    p.drawString(100, 750, "Name")
    p.drawString(200, 750, "Amount")
    p.drawString(300, 750, "Category")
    p.drawString(400, 750, "Transaction Type")
    p.drawString(500, 750, "Created At")

   
    transactions = Transaction.objects.all()
    y_position = 730

    
    for transaction in transactions:
        p.drawString(100, y_position, transaction.name)
        p.drawString(200, y_position, str(transaction.amount))
        p.drawString(300, y_position, transaction.category)
        p.drawString(400, y_position, transaction.get_transaction_type_display())
        p.drawString(500, y_position, str(transaction.created_at))

        y_position -= 20

   
    p.showPage()
    p.save()
    return response


class RecommendationEngine:
    def __init__(self, balance):
        self.balance = balance
    
    def get_recommendations(self):
        recommendations = []
    
        if self.balance < 0:
            recommendations.append("Your balance is negative. Try to cut down on expenses.")
        elif self.balance == 0:
            recommendations.append("You have no funds. Consider saving for future expenses.")
        elif 0 < self.balance <= 100:
            recommendations.append("Your balance is low. Try reducing spending in categories like shopping and entertainment.")
        elif 100 < self.balance <= 500:
            recommendations.append("Your balance is healthy. Consider saving some money for future needs.")
        elif self.balance > 500:
            recommendations.append("You have a good balance! Consider investing or saving more for future opportunities.")
        
        return recommendations