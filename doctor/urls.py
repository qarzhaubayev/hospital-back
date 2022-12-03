from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('doctors/',     DoctorList.as_view(), name='doctors'),
    path('doctor/<pk>/', DoctorRUD.as_view(),  name='doctor'),
    path('doctors/<specialization>/<int:limit>/<int:offset>/', DoctorIINList.as_view(), name='doctors_spec_limit'),
    path('doctors/<specialization>', DoctorIINList.as_view(), name='doctors_spec'),
]
