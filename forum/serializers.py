from .models import *
from rest_framework import serializers

# 论坛
class ForumSer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'