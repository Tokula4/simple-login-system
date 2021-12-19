from django.urls import path
from django.urls import path, include 
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('', views.accounts, name = 'accounts'),
    path('home/', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('accounts/', include('allauth.urls')), 
    
    
   
   
]