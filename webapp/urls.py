from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('showcase/', views.Showcase.as_view(), name='showcase'),
    path('add_build/', views.AddBuild.as_view(), name='add_build'),
]
