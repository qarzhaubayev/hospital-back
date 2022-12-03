# Create your views here.
from django.shortcuts import Http404
from django.http import HttpResponse,JsonResponse

from rest_framework import generics
from rest_framework import status

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions    import IsAuthenticated, IsAdminUser
from rest_framework.response       import Response

from .models      import *
from .serializers import *

class PatientList(generics.ListCreateAPIView):
    queryset               = Patient.objects.all()
    serializer_class       = PatientSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, format=None):
        print(request.auth)
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset               = Patient.objects.all()
    serializer_class       = PatientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, pk, format=None):
        print(request.auth)
        try:
            patient = Patient.objects.get(iin = pk)
        except Patient.DoesNotExist:
            raise Http404('Not found')
        serializer = PatientSerializer(patient)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        try:
            patient = Patient.objects.get(iin = pk)
        except Patient.DoesNotExist:
            raise Http404('Not found')
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
