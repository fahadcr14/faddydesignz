from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('service.html', views.service, name=''),
    path('contact.html', views.contact, name=''),
    path('aboutus.html', views.about, name=''),
    path('dashboard.html', views.dashboard, name=''),
    path('contactdetails.html', views.contactdetails, name=''),

    path('realtime_views', views.realtime_views_api, name=''),
    path('inserting_responded', views.inserting_responded, name=''),

    #apis
    path('contactsubmission/', views.contact_submission, name='/contactsubmission/'),
    #---------------------------------authentication--------------------------------
    path('auth.html', views.auth, name='auth'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login_view/', views.login_vieww, name='login_views'),
    ]
