from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('showcase/', views.Showcase.as_view(), name='showcase'),
]
