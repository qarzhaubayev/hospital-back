from django.contrib import admin
from django.urls import path
from .models import Doctor
from .views import obtain_auth_token
from django.urls import path, include
from .views import *
# from .views import PatientList, PatientRUD



urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('doctors/',     DoctorList.as_view(), name='doctors'),
    path('doctor/<pk>/', DoctorRUD.as_view(),  name='doctor'),
    path('doctors/<specialization>/<int:limit>/<int:offset>/', DoctorIINList.as_view(), name='doctors_spec_limit'),
    path('doctors/<specialization>', DoctorIINList.as_view(), name='doctors_spec'),
        path('patients/',     PatientList.as_view(), name='patientRUD'),
    path('patient/<pk>/', PatientRUD.as_view(),  name='patient'),

]
