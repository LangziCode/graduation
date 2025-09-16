from .models import *
from rest_framework import serializers

class ExamrecordSer(serializers.ModelSerializer):
    class Meta:
        model = Examrecord
        fields = '__all__'