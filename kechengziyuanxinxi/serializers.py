from .models import *
from rest_framework import serializers

class KechengziyuanxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Kechengziyuanxinxi
        fields = '__all__'