from django.db import models

class Coarse(models.Model):
    coarse_id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.DateField()
    author = models.CharField( max_length=50)