from django.urls import path
from . import views

urlpatterns = [
     path('', views.Home.as_view(), name='home'),
     path('showcase/', views.Showcase.as_view(), name='showcase'),
     path('my_garage/', views.MyGarage.as_view(), name='my_garage'),
     path('add_build/', views.AddBuild.as_view(), name='add_build'),
     path('edit_build/<int:pk>/',
          views.EditBuild.as_view(), name='edit_build'),
     path('delete_build/<int:build_id>/',
          views.delete_build, name='delete_build'),
     path('<slug:slug>/', views.BuildDetail.as_view(), name="build_detail"),
     path('delete_comment/<int:comment_id>',
          views.delete_comment, name='delete_comment'),
     path('like/<slug:slug>/', views.BuildLike.as_view(), name='build_like'),
     path('save/<slug:slug>/', views.BuildSave.as_view(), name='build_save'),
]
