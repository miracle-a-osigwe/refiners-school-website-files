from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import SignUpView, LoginView, UserView

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile/', login_required(UserView.as_view()), name='profile'),
    #path("signup/", SignUpView.as_view(), name="signup"),
    #path("login/", LoginView.as_view(), name="login"),
]