from .models import *
from rest_framework import serializers

class AddressSer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'