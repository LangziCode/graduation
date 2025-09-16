from .models import *
from rest_framework import serializers

# 私信
class LetterSer(serializers.ModelSerializer):
    sender = serializers.IntegerField()
    senderName = serializers.CharField(source='sender_name')
    receiver = serializers.IntegerField()
    receiverName = serializers.CharField(source='receiver_name')
    msg = serializers.CharField()
    sendTime = serializers.DateTimeField(source='send_time')
    readStatus = serializers.IntegerField(source='read_status')

    class Meta:
        model = Letter
        fields = ['sender', 'senderName', 'receiver', 'receiverName', 'msg', 'sendTime', 'readStatus']  # 指定新字段