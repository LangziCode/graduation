from .models import *
from rest_framework import serializers

class DiscusskechengziyuanxinxiSer(serializers.ModelSerializer):
    class Meta:
        model = Discusskechengziyuanxinxi
        fields = '__all__'