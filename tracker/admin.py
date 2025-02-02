from django.contrib import admin
from .models import  Transaction, UserBalance


admin.site.register(Transaction)
admin.site.register(UserBalance)