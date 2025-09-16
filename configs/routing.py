# routing.py
# 在 Django 中，WebSocket 的路由通过 routing.py 文件配置

from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path('py003/consultation', consumers.DoctorUserWebSocketConsumer.as_asgi()),
    path('py003/letter', consumers.LetterWebSocketConsumer.as_asgi()),
]