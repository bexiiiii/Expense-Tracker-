from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Transaction

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label="Электронная почта")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    # Переопределение метода clean, если нужно добавить дополнительную логику
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Здесь можно добавить дополнительную проверку или логирование
        return cleaned_data

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['name', 'amount', 'category', 'transaction_type']