import email
from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from banking.models import BankAccount, Transactions
from django.utils.crypto import get_random_string as g
import requests



class Command(BaseCommand):
    help = '''Populates the db with dummy data. To create credit bank accounts for users created with the
    'create_users' command. This should be run in a new terminal and after creating users.
        Django server must be running, so please run in a new terminal'''

    def handle(self, *args, **kwargs):
        url = 'http://127.0.0.1:8000/createtransactionapi/'
        
        number_of_users = 5

        for id in range(number_of_users+1):
            data = {
                'transaction_type': 'withdrawal',
                'transaction_amount': 200,
                'account_type': id, 'user': id}
            
            response = requests.post(url, data=data)

        self.stdout.write(self.style.SUCCESS('Withdrawal done for accounts of {} users successfully'.format(number_of_users)))
        
