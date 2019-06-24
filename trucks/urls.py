from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.indexview , name='home'),
    path('home/', views.homepage, name='start'),
    path('about/', views.aboutpage, name='about'),
    path('contactme/', views.contactme, name='contactus'),
    path('accounts/',views.accounts, name='accounts'),
    path('newtruck/',views.newtruck, name='newtruck')
    
]
