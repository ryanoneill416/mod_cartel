from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('showcase/', views.Showcase.as_view(), name='showcase'),
    path('my_garage/', views.MyGarage.as_view(), name='my_garage'),
    path('add_build/', views.AddBuild.as_view(), name='add_build'),
    path('edit_build/<int:pk>', views.EditBuild.as_view(), name='edit_build'),
]
