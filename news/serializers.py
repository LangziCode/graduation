from .models import *
from rest_framework import serializers

class NewsSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'