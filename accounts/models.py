from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator
from django.utils.functional import cached_property
from django.urls import reverse



class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password= None, ):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(
            email = self.normalize_email(email),
              )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using = self.db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None,):
        if not email:
            raise ValueError('Email is Required')
        user = self.create_user(
            email = self.normalize_email(email),
            password=password, first_name =first_name, last_name=last_name
              )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.first_name = first_name
        user.last_name = last_name
        user.save(using = self.db)
        return user


class CustomUser(AbstractUser):
    
    username = None
    first_name = models.CharField(verbose_name='First Name', max_length=100, )
    last_name = models.CharField(verbose_name='Last Name', max_length=100, )
    email = models.EmailField(db_index=True, unique=True,)
    
    
    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name' ]
    EMAIL_FIELD = 'email'


    class Meta:
        ordering = ['-date_joined']


    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


