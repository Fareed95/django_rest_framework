from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Coarse
from .serializers import CoarseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse('hello worlds')

class CoarseList(APIView):
    def get(self ,request):
        coarse = Coarse.objects.all()
        serializer = CoarseSerializer(coarse,many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CoarseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.error, status = status.HTTP_403_FORBIDDEN)
        
class CoarseDetailview(APIView):
    def get_coarse(self,pk):
        try :
            return Coarse.objects.get(pk=pk)
        except Coarse.DoesNotExist :
            raise Http404

    def get(self, request,pk):
        coarse = self.get_coarse(pk)
        serializer = CoarseSerializer(coarse)
        return Response(serializer.data)
    
    def put(self,request,pk):
        coarse = self.get_coarse(pk)
        serializer = CoarseSerializer(coarse,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.error, status = status.HTTP_403_FORBIDDEN)
    
    def delete(self , request ,pk):
        self.get_coarse(pk).delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
        

        
            
