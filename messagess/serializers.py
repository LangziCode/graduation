from .models import *
from rest_framework import serializers

class MessagessSer(serializers.ModelSerializer):
    class Meta:
        model = Messagess
        fields = '__all__'