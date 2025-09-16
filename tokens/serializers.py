from .models import *
from rest_framework import serializers

# token表
class TokenSer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'