from .models import Employee
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Employee
        fields = '__all__'
class UsersSerializer(serializers.ModelSerializer):
 class Meta:
    model = User 
    fields = '__all__'

    