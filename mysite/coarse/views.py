from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Coarse
from .serializers import CoarseSerializer
from rest_framework import status
# Create your views here.
def index(request):
    return JsonResponse({"message":"success"})


@api_view(['GET','POST'])
def CoarseView(request):
    if request.method == 'GET':
        coarse = Coarse.objects.all()
        serializer = CoarseSerializer(coarse,many = True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CoarseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

@api_view(['PUT','GET','DELETE'])
def Coarse_personal(request, pk ):
    try :
        coarse = Coarse.objects.get(pk=pk)
    except Coarse.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)        
    if request.method == 'PUT':
        serializer = CoarseSerializer(coarse,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
    elif request.method=='GET':
        serializer = CoarseSerializer(coarse)
        return Response(serializer.data)
    elif request.method =='DELETE':
        coarse.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)