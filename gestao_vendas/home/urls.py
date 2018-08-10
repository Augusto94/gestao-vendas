from django.contrib import admin
from django.urls import path
from .views import home, login, logout

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout, name='logout')
]
