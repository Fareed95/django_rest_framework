from rest_framework import serializers
from . models import Coarse


class CoarseSerializer(serializers.ModelSerializer):
    class Meta :
        model = Coarse
        fields = "__all__"