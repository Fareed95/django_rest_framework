from django.shortcuts import render
from .models import Coarse,Instructor
from .serializers import CoarseSerializer,InstructorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics



class InstructorView(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CoarseView(generics.ListCreateAPIView):
    queryset = Coarse.objects.all()
    serializer_class = CoarseSerializer
