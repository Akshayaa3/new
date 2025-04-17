from django.contrib import admin
from django.urls import path
from kct import views#achu
#achu
urlpatterns = [
    path('loginPage/', views.loginPage,name='loginpage'),
]
