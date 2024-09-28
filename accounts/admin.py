from django.contrib import admin
from .models import Customer, Account, Transaction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'customer', 'balance', 'created_at')
    search_fields = ('account_number', 'customer__first_name', 'customer__last_name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'date')
    search_fields = ('account__account_number', 'transaction_type')
    list_filter = ('transaction_type', 'date')
    ordering = ('-date',)
