"""
URL configuration for Oasis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from Oasis.views import Games
from . import views
from users.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="account/login.html")),
    path('accounts/google/con/', TemplateView.as_view(template_name="account/Lgoogle.html")),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("chat/", views.IA),    
    path('Games/', Games),
    path('admin/', admin.site.urls),    
    path('accounts/', include('allauth.urls')),
]
