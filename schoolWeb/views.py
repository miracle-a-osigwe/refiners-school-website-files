from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from mcq.models import Assessment
from django.contrib.auth import get_user_model
from django.shortcuts import render


User = get_user_model()

app_name = 'school'

class UserProfile(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'user_profile.html'

class IndexView():
    pass