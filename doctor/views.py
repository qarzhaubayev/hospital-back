# Create your views here.
from django.shortcuts import Http404
from django.http import HttpResponse,JsonResponse




from rest_framework.pagination     import LimitOffsetPagination
from rest_framework.response       import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions    import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework import generics

from .serializers import *
from .models import *


class DoctorIINList(generics.ListAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]
    pagination_class       = LimitOffsetPagination

    def get(self, request, specialization, limit, offset, format=None):
        print("auth:", request.auth)
        print("spec:", specialization)
        doctors    = Doctor.objects.filter(specialization__iexact=specialization).values('iin')
        count      = doctors.count()
        to_return  = doctors[offset:offset+limit]
        serializer = DoctorIINSerializer(to_return, many=True)
        return Response({'doctors': serializer.data, 'count': count})#JsonResponse(serializer.data, safe=False)

class DoctorList(generics.ListCreateAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes     = [IsAdminUser,]

    def get(self, request, format=None):
        print(request.auth)
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.auth)
        print(request.data)
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset               = Doctor.objects.all()
    serializer_class       = DoctorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAdminUser,]
    
    def delete(self, request, pk, format=None):
        try:
            doctor = Doctor.objects.get(iin = pk)
        except Doctor.DoesNotExist:
            raise Http404('Not What found')
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.delete()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        print(request.auth)
        try:
            doctor = Doctor.objects.get(iin = pk)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format=None):
        try:
            doctor = Doctor.objects.get(iin = pk)
        except Doctor.DoesNotExist:
            raise Http404('Not found')
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
