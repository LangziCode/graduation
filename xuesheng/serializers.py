from .models import *
from rest_framework import serializers

class XueshengSer(serializers.ModelSerializer):
    class Meta:
        model = Xuesheng
        fields = '__all__'