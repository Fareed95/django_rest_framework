from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Instructor(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.email
class Coarse(models.Model):
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.DateField()
    instructor= models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name= 'coarse')
    