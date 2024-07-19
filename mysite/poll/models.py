from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    phone = PhoneNumberField()
    def __str__(self) :
        return self.name 