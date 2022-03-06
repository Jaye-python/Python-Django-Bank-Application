"""bankapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as av
from banking import views as bv
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # CREATE NEW USER VIA API
    path('register/', av.CreateCustomUser.as_view()),

    # API ENDPOINT TO SHOW ACCOUNT DETAILS FOR LOGGED-IN USER USING CUSTOMUSER SERIALIZER
    path('viewuseraccount/', av.ViewUserAccount.as_view()),

    # ADMIN VIEW TO SHOW ACCOUNT DETAILS FOR SPECIFIC USER ID
    path('adminviewuser/<id>/', av.AdminViewUser.as_view()),
    
    # CREATE BANK ACCOUNT VIA API
    path('createbankaccountapi/', bv.CreateBankAccountAPI.as_view()),

    # UPDATE BANK ACCOUNT VIA API
    path('bankaccountupdate/<int:pk>/', bv.BankAccountUpdate.as_view()),

    # MAKE DEPOSITS AND WITHDRAWALS VIA API
    path('createtransactionapi/', bv.CreateTransactionAPI.as_view()),

    # VIEW ACCOUNT DETAILS FOR CUSTOMER VIA CURL COMMAND. MUST PROVIDE ADMIN USERNAME:PASSWORD
        # curl -u bb@bb.com:123456  http://127.0.0.1:8000/viewbankaccountapi/?id=10
    path('viewbankaccountapi/', bv.ViewBankAccountAPI.as_view()),

    # API ENDPOINT TO SHOW ACCOUNT DETAILS FOR LOGGED-IN USER USING BANKACCOUNT SERIALIZER
    path('viewbankaccountuser/', bv.ViewBankAccountUser.as_view()),
    
    # CSV DOWNLOAD
    path('downloadbankaccounts/', bv.downloadBankAccounts),


    
    # DRF AUTH
    path('api-auth/', include('rest_framework.urls')),

    # DRF DOCS
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('openapi/', get_schema_view(
        title="Python Django Bank App",
        description="An API-based Banking app"
    ), name='openapi-schema'),

]


