from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from users import views
urlpatterns = [
    path('', views.register, name = 'lastshop-register'),
    #path('about/', views.about, name = 'lastshop-about'),
]