from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics
from rest_framework import permissions


# CREATE NEW USER VIA API

class CreateCustomUser(generics.CreateAPIView):
    '''
    CURL COMMAND TO CREATE NEW USER
    curl --data "email=newuser@pp.com&first_name=newuserfirstname&last_name=newuserfirstname&password=1234" http://127.0.0.1:8000/register/

    URL: http://127.0.0.1:8000/register/
    '''
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# API ENDPOINT TO SHOW ACCOUNT DETAILS FOR LOGGED-IN USER USING CUSTOMUSER SERIALIZER

class ViewUserAccount(generics.ListAPIView):
    '''
    VIEW ACCOUNT INFO FOR LOGGED IN USER:\n
    URL: 'http://127.0.0.1:8000/viewuseraccount/'
    
    '''
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        logged_in_user = self.request.user.id  
        queryset = CustomUser.objects.filter(id = logged_in_user)
        return queryset


# ADMIN VIEW TO SHOW ACCOUNT DETAILS FOR SPECIFIC USER ID
class AdminViewUser(generics.ListAPIView):
    '''
    VIEW ACCOUNT INFO FOR SPECIFIC USER. (in the case below details of user with id 8 will be shown):
    http://127.0.0.1:8000/adminviewuser/8/

    I HAVE ALSO CONFIGURED DJANGO ADMIN URL TO DO SAME THING: 
    http://127.0.0.1:8000/admin/
    
    '''
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
        
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = CustomUser.objects.filter(id = id)
        return queryset