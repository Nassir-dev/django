from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='start'),
    path('about/', views.aboutpage, name='about'),
    path('contactme/', views.contactme, name='contactus'),
    
    


    path('about/', views.aboutpage, name='about'),
    path('contactme/', views.contactme, name='contactus'),
    path('accounts/',views.accounts, name='accounts'),
    path('newclient/',views.newclient,name='new'),
    path('new_invoice/',views.invoice,name='newinvoice'),
    path('new_payment/',views.newclient,name='payment')

    
]
