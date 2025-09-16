from .models import *
from rest_framework import serializers

class DiscusskechengxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Discusskechengxinxi
        fields = '__all__'