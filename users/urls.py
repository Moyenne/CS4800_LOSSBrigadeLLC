from django.contrib import admin
from django.urls import path, include
from django.urls import path
import users
from . import views
from users import views

urlpatterns = [
    path('', views.register, name = 'lastshop-register'),
    #path('', views.loginls, name = 'login'),
    #path('about/', views.about, name = 'lastshop-about'),
]