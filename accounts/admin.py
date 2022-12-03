from django.contrib import admin
from .models import Doctor
from .models import Patient

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)

