from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer,UsersSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1 style = 'color: blue' class = 'nigga'>yes this nigga shiit is working</h1> ")
    
@csrf_exempt
def Employeelistview(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many= True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='POST':
        return JsonResponse({'message':'kaam kar raha hai bacchi'})


def userlistview(request):
    employee = User.objects.all()
    serializer = UsersSerializer(employee, many =True)
    return JsonResponse(serializer.data, safe=False)