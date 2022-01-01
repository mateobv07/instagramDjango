from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('profile/', views.UserList.as_view()),
    path('profile/<str:pk>', views.UserDetail.as_view()),
]