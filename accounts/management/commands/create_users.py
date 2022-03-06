import email
from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from django.utils.crypto import get_random_string as g
import string as s



class Command(BaseCommand):
    help = 'Populates the db with dummy data. Only to create Users'

    def handle(self, *args, **kwargs):
        
        number_of_users = 5
        
        for i in range(number_of_users):
            CustomUser.objects.create_user(
                email = g(4, allowed_chars=s.ascii_lowercase)+'@gmail.com',
                first_name=g(4, allowed_chars=s.ascii_lowercase),
                last_name=g(4, allowed_chars=s.ascii_lowercase),
                password='1234')

        self.stdout.write(self.style.SUCCESS('{} users created successfully'.format(number_of_users)))
