from .models import *
from rest_framework import serializers

# 论坛
class StoreupSer(serializers.ModelSerializer):
    class Meta:
        model = Storeup
        fields = '__all__'