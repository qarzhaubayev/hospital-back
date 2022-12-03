from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Patient
from .models import Doctor
from django.contrib.auth.hashers import make_password

class DoctorIINSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["iin_num"]

class DoctorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(DoctorSerializer, self).create(validated_data)

    class Meta:
        model = Doctor
        fields = ["name", "surname", "midname", "birthday_date", "iin_num", "id", "education", "departament_id", "specialize", "category", "photo", "schedule", "appointment_duration", "price", "contact_number", "experience", "address", "password"]


class PatientSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(PatientSerializer, self).create(validated_data)

    class Meta:
        model = Patient
        fields = ["name", "surname", "middlename", "birthday_date", "iin_num", "id", "blood_type", "marital_status", "contact_number", "emergency_contact_number", "email", "address", "password"]

