from django.contrib import admin
from django.urls import path, include
from .views import PatientList, PatientRUD

urlpatterns = [
    path('patients/',     PatientList.as_view(), name='patientRUD'),
    path('patient/<pk>/', PatientRUD.as_view(),  name='patient'),
]
