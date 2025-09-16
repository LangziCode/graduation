from .models import *
from rest_framework import serializers

class KechengxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Kechengxinxi
        fields = '__all__'