from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    # path('admission/', views.AdmissionView.as_view(), name='admission'),
    path('admission/', views.submit_form, name='admission'),
    path('academics/', views.AcademicView.as_view(), name='academics'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('alumni/', views.AlumniView.as_view(), name='alumni'),
    path('resources/', views.ResourcesView.as_view(), name='resources'),
    # path('staff/', views.StaffView.as_view(), name='staff'),
    # path('student/', views.StudentView.as_view(), name='student'),
    path('facilities/', views.FacilityView.as_view(), name='facilities'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)