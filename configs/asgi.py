# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing  # 导入路由配置

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP 请求
    "websocket": URLRouter(
        routing.websocket_urlpatterns  # WebSocket 路由
    ),
})