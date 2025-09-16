from .models import *
from rest_framework import serializers

class ExampaperSer(serializers.ModelSerializer):
    class Meta:
        model = Exampaper
        fields = '__all__'