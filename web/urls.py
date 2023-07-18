from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('service.html', views.service, name=''),
    path('contact.html', views.contact, name=''),
    
    #apis
    path('contactsubmission/', views.contact_submission, name='/contactsubmission/'),
    ]
