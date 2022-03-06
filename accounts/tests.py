from django.test import TestCase
from .models import CustomUser
from django.utils.crypto import get_random_string as g
import string as s
from banking.models import BankAccount

# TO RUN TESTS, DJANGO SERVER MUST BE RUNNING SO PLEASE LAUNCH TEST IN A NEW TERMINAL WHILE SERVER IS RUNNING

class BankAppTestCase(TestCase):

    def setUp(self):
        self.user_account_for_test = CustomUser.objects.create_user(
            email=g(4, allowed_chars=s.ascii_lowercase)+'@gmail.com',
            first_name=g(4, allowed_chars=s.ascii_lowercase),
            last_name=g(4, allowed_chars=s.ascii_lowercase),
            password='1234'
              )

        self.bank_account_for_test = BankAccount.objects.create(
            account_type= 'credit',
            user=self.user_account_for_test
            )
        
        

    # CREATE NEW USER VIA API TEST
    
    def test_create_new_users_via_api(self):
        """Test if users can be created via API:
        http://127.0.0.1:8000/register/
        """
        
        url = 'http://127.0.0.1:8000/register/'
        data = {
            'email': g(4, allowed_chars=s.ascii_lowercase)+'@gmail.com',
            'first_name': g(4, allowed_chars=s.ascii_lowercase),
            'last_name' : g(4, allowed_chars=s.ascii_lowercase),
            'password' : '1234'
        }
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
    

    # CREATE BANK ACCOUNT VIA API TEST
        # CREATE CREDIT ACCOUNT TEST

    def test_create_credit_bank_account_via_api(self):
        """Test if credit bank accounts can be created via API:
        
        'http://127.0.0.1:8000/createbankaccountapi/'
        """
        
        url = 'http://127.0.0.1:8000/createbankaccountapi/'
        data = {'account_type': 'credit', 'user': self.user_account_for_test.id}
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
    
        # CREATE SAVINGS ACCOUNT TEST

    def test_create_savings_bank_account_via_api(self):
        """Test if savings bank accounts can be created via API:
        
        'http://127.0.0.1:8000/createbankaccountapi/'
        """
        
        url = 'http://127.0.0.1:8000/createbankaccountapi/'
        data = {'account_type': 'savings', 'user': self.user_account_for_test.id}
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
    

    # MAKE DEPOSITS AND WITHDRAWALS VIA API TEST

    def test_make_deposit_via_api(self):
        """Test if deposists can be made via API:
        
        http://127.0.0.1:8000/createtransactionapi/
        -data "transaction_type=deposit&transaction_amount=10&account_type=21&user=10" http://127.0.0.1:8000/createtransactionapi/
        """
        
        url = 'http://127.0.0.1:8000/createtransactionapi/'
        data = {
            'transaction_type': 'deposit', 'transaction_amount': 200,
            'account_type': self.bank_account_for_test.id, 'user': self.user_account_for_test.id}
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
    

    def test_make_withdrawal_via_api(self):
        """Test if withdrawals can be made via API:
        
        http://127.0.0.1:8000/createtransactionapi/
        -data "transaction_type=deposit&transaction_amount=10&account_type=21&user=10" http://127.0.0.1:8000/createtransactionapi/
        """
        
        url = 'http://127.0.0.1:8000/createtransactionapi/'
        data = {
            'transaction_type': 'withdrawal', 'transaction_amount': 1000,
            'account_type': self.bank_account_for_test.id, 'user': self.user_account_for_test.id}
        
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)