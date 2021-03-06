"""models path Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a path to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from trucks import views as trucks_views
from users import views as user_views
from client_app import views as client_views
from accounts_app import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trucks_views.homepage, name='home'),
    path('signup/',user_views.signup_view, name='sign_up'),
    path('login/',user_views.login_view, name='log_in'),
   
]
