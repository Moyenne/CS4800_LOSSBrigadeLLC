from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'lastshop-home'),
    path('about/', views.about, name = 'lastshop-about'),
]