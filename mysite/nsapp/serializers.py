from rest_framework import serializers
from . models import Coarse,Instructor



class CoarseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coarse
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    # here the name coarse should perfectly written as in models.py related_name is mentioned as coarse 
    coarse = CoarseSerializer(many = True, read_only = True)
    class Meta :
        model = Instructor
        fields = '__all__'