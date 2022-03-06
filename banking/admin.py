from dataclasses import fields
from django.contrib import admin
from accounts.models import CustomUser
from banking.models import BankAccount, Transactions

# Register your models here.

class BankAccountInline(admin.StackedInline):
    model = BankAccount
    can_delete= False
    verbose_name_plural = 'Customer bank accounts'
    fk_name = 'user'
    extra = 0
    # form = No form

    readonly_fields = ['account_type', 'account_balance', 'date']


class TransactionsInline(admin.TabularInline):
    model = Transactions
    can_delete= False
    verbose_name_plural = 'transactions'
    fk_name = 'user'
    extra = 0
    
    # form = No form

    readonly_fields = ['account_type',  'transaction_type', 'transaction_amount', 'transaction_date', 'date_created'
    ]


class CustomUserAdmin(admin.ModelAdmin):
    
    readonly_fields = ['date_joined', 'last_login', 'email', 'first_name', 'last_name', 
    ]

    fieldsets = (
        ('Customer Info', {'fields': ( 'email', 'first_name', 'last_name', )}),
        (
        'Advanced options', {
            'classes': ('collapse', ),
        
        
        'fields': ('date_joined', 'last_login',),
        }),)

    list_filter = ['email']
    search_fields = ['email']
    inlines = (BankAccountInline, TransactionsInline )
    


admin.site.register(CustomUser, CustomUserAdmin )