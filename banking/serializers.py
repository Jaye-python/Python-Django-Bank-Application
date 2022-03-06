from rest_framework import serializers
from accounts.models import CustomUser
from .models import BankAccount, Transactions



class TransactionSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),many=False,)
    account_type = serializers.PrimaryKeyRelatedField(queryset=BankAccount.objects.all(),many=False,)
    
    class Meta:
        model = Transactions
        fields = [ 'id', 'transaction_date', 'account_type', 'user', 'transaction_type', 'transaction_amount', ]
        


class BankAccountSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),many=False,)
    accounttransactions = TransactionSerializer(many=True, read_only=True, )
    
    class Meta:
        model = BankAccount
        fields = ['id', 'date', 'account_type', 'user', 'account_balance', 'accounttransactions']
        extra_kwargs = {
            'account_balance': {'read_only': True},
            
            }