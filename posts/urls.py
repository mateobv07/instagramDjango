from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('myPosts/', views.profilePosts.as_view()),
    path('mySaved/', views.ProfileSaved.as_view()),
    path('mytags/', views.ProfileTagged.as_view()),
    path('myPosts/<str:username>/', views.UserPosts.as_view()),
    path('userTags/<str:username>/', views.UserTags.as_view()),

]