from .models import *
from rest_framework import serializers

class CartSer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'