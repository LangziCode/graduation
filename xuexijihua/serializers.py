from .models import *
from rest_framework import serializers

class XuexijihuaSer(serializers.ModelSerializer):
    class Meta:
        model = Xuexijihua
        fields = '__all__'