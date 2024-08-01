from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse as hr
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate

# Create your views here.
User = get_user_model()


# from .models import User

# app name
app_name = 'accounts'


class UserView(generic.DetailView):
    template_name = 'accounts/profile.html'
    context_object_name = 'object'

    def get_object(self):
        return self.request.user.firstName

class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request)
        #resp = mb.authenticate(self, request, username=username, password=password)
        print(username, password, user)
        
        return hr("Successful")

class SignUpView(generic.DetailView):
    template_name = 'accounts/signup.html'