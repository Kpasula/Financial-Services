from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import DateTimeInput, DateInput

from .models import Customer, Stock, Investment, MutualFund


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'income')


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)
        widgets = {
            'purchase_date': DateInput(attrs={'type': 'date'}),
        }


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
                  'recent_date',)
        widgets = {
            'acquired_date': DateInput(attrs={'type': 'date'}),
            'recent_date': DateInput(attrs={'type': 'date'}),
        }


class MutualFundForm(forms.ModelForm):
    class Meta:
        model = MutualFund
        fields = ('customer', 'plan', 'investment_amount', 'current_value', 'acquired_date',)
        widgets = {
            'acquired_date': DateInput(attrs={'type': 'date'}),
        }