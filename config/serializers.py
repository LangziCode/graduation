from .models import *
from rest_framework import serializers

# 轮播图
class ConfigSer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'
