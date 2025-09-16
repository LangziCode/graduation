from .models import *
from rest_framework import serializers

class ExamquestionSer(serializers.ModelSerializer):
    class Meta:
        model = Examquestion
        fields = '__all__'