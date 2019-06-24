from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.indexview , name='home'),
    path('home/', views.homepage, name='start'),
    path('about/', views.aboutpage, name='about')
    path('contact/', views.contact, name='contact')
    
]
