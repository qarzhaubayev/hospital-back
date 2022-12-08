from django.db import models

# Create your models here.
class Patient(models.Model):
    iin = models.CharField(max_length= 12,unique=True)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    middlename = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12, null=True)
    emergency_contact = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    blood_group = models.CharField(max_length=5, null=True)
    maritual_status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    iin = models.CharField(max_length= 12, unique=True)
    name           = models.CharField(max_length=200, null= True)
    surname        = models.CharField(max_length=200, null= True)
    middlename     = models.CharField(max_length=200, null= True)
    birthday         = models.DateField(null= True)
    phone_number = models.CharField(max_length=12, null= True)
    email = models.EmailField(max_length=50, null=True)
    experience     = models.CharField(max_length=3, null= True)
    url            = models.CharField(max_length=200, blank=True, null= True)
    address        = models.CharField(max_length=200,null= True)
    education      = models.CharField(max_length=3, null= True)
    departament    = models.CharField(max_length=200, null= True)
    specialization = models.CharField(max_length=200, null= True)
    category       = models.CharField(max_length=200, null= True)
    photo          = models.FileField(upload_to='images/', null= True)
    
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctorname = models.CharField(max_length=50, null=True)
    doctoremail = models.EmailField(max_length=50, null=True)
    patientname = models.CharField(max_length=50, null=True)
    patientemail = models.CharField(max_length=50, null=True)
    appointmentdate = models.DateField()
    appointmenttime = models.TimeField()
    symptoms = models.CharField(max_length=50, null=True)
    prescriptions = models.CharField(max_length=200, null=True)
    status = models.BooleanField()
    
    def __str__(self):
        return "Patient "+  self.patientname + " have appointment with " + " Doctor "+ self.doctorname + " on "+ str(self.appointmentdate) + " at " + str(self.appointmenttime)