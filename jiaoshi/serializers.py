from .models import *
from rest_framework import serializers

class JiaoshiSer(serializers.ModelSerializer):
    class Meta:
        model = Jiaoshi
        fields = '__all__'