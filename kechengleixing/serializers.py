from .models import *
from rest_framework import serializers

class KechengleixingSer(serializers.ModelSerializer):
    class Meta:
        model = Kechengleixing
        fields = '__all__'