"""schoolWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import UserProfile
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    re_path(r'home/', include('core.urls', namespace='webpage')), #### This will be used when the project is near completion.
    # path('admin/signup', TemplateView.as_view(template_name="main/signup.html"), name='signup'),
    # re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
