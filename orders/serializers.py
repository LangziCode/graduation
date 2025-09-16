from .models import *
from rest_framework import serializers

class OrdersSer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'