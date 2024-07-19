from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import Coarse
from .serializers import CoarseSerializer
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is the name of the http response")

class Coarse(ModelViewSet):
    queryset = Coarse.objects.all()
    serializer_class = CoarseSerializer
