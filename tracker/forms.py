from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Transaction

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label="Электронная почта")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

       
        return cleaned_data

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'category', 'transaction_type']
        
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Ошибка: сумма должна быть больше нуля.", code='invalid')
        return amount
