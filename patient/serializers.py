from rest_framework import serializers
from .models import Patient
from django.contrib.auth.hashers import make_password

class PatientSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(PatientSerializer, self).create(validated_data)
    class Meta:
        model = Patient
        fields = ["name", "surname", "middlename", "bddate", "iin", "id", "blood_type", "marital_status", "contact_number", "emergency_contact_number", "email", "address", "password"]

