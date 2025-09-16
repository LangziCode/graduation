from .models import *
from rest_framework import serializers

# 管理员表
class UsersSer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
