from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('myPosts/', views.profilePosts.as_view()),
    path('mySaved/', views.ProfileSaved.as_view()),

]