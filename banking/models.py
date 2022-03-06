from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.functional import cached_property
from django.urls import reverse
from django.conf import settings


class BankAccount(models.Model):
    account_type = (
        ('savings', 'Savings'),
        ('credit', 'Credit'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='bankaccount', on_delete=models.CASCADE, )
    account_type = models.CharField(max_length=20, choices=account_type, db_index=True )
    account_balance = models.FloatField(default=0)
    date = models.DateTimeField(auto_now=True, verbose_name='Transaction Date')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.account_type

    def get_absolute_url(self):
        return reverse('bank-detail', kwargs={'pk': self.pk})

    

class Transactions(models.Model):

    transaction_type = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transactions', on_delete=models.CASCADE, )
    account_type = models.ForeignKey(BankAccount, related_name='accounttransactions', to_field='id', on_delete=models.CASCADE,)
    transaction_type = models.CharField(max_length=20, choices=transaction_type)
    transaction_amount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now=True, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-transaction_date']


    def __str__(self):
        return self.transaction_type

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})