from django.urls import path
from . import views

urlpatterns = [
    path('', views.LaunchPage, name = 'lastshop-home'),
    path('about/', views.about, name = 'lastshop-about'),
    path('HomePage/', views.homepage, name='lastshop-homepage'),

]