from django.contrib import admin
from django.urls import path, include
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('login/', obtain_auth_token, name="login"),
    path('profile/', views.UserList.as_view()),
    path('profile/<str:username>', views.UserDetail.as_view()),
    path('myprofile/', views.myProfile.as_view()),
]