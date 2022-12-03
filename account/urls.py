from django.contrib import admin
from django.urls import path
from .views import obtain_auth_token

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
]
