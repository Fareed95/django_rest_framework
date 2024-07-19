from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer,UsersSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1 style = 'color: blue' class = 'nigga'>yes this nigga shiit is working</h1> ")
    
@api_view (['GET','POST'])
def Employeelistview(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many= True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )
@api_view (['DELETE','GET','PUT'])
def EmployeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist :
        return Response(status = 404)
    # print(employee)
    
    if request.method == "DELETE":
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data )
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else :
            return Response(serializer.errors )


@api_view(['GET'])
def userlistview(request):
    if request.method == 'GET':
        employee = User.objects.all()
        serializer = UsersSerializer(employee, many =True)
        return Response(serializer.data)