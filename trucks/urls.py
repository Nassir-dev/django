from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.indexview , name='home'),
    path('home/', views.homepage, name='start'),
<<<<<<< HEAD
    path('about/', views.aboutpage, name='about')
    path('contact/', views.contact, name='contact')
=======
    path('about/', views.aboutpage, name='about'),
    path('contactme/', views.contactme, name='contactus'),
    path('accounts/',views.accounts, name='accounts'),
    
>>>>>>> 35b482bb002a393002b6fbcbcd9352e85afbb7d9
    
]
