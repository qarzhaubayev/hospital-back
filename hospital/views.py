from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'homepage.html')

def doctor(request):
    return render(request, 'accounts/doctor.html')
def patient(request):
    return render(request, 'accounts/patient.html')