from . import views
from django.urls import path, include
from .views import CustomLoginView


urlpatterns = [
    path("", views.main, name="home"),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('export_transactions/', views.export_transactions, name='export_transactions'),
    path('export_transactions_pdf/', views.export_transactions_pdf, name='export_transactions_pdf'),

]
