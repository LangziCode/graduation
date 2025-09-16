# consumers.py
# 我们可以创建两个消费者，分别对应 /consultation 和 /letter

# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone

from consultation.models import Consultation
from letter.models import Letter


class DoctorUserWebSocketConsumer(AsyncWebsocketConsumer):
    # 存储用户会话的字典
    role_session_map = {}

    async def connect(self):
        # 获取 URL 参数
        query_params = self.scope['query_string'].decode('utf-8')
        params = {k: v for k, v in [param.split('=') for param in query_params.split('&')]}
        role = params.get('role')
        user_id = int(params.get('userid'))
        nickname = params.get('nicheng')

        # 将用户会话存储到字典中
        if role not in self.role_session_map:
            self.role_session_map[role] = {}
        self.role_session_map[role][(user_id, nickname)] = self

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 从字典中移除用户会话
        for role, user_sessions in self.role_session_map.items():
            for key, session in user_sessions.items():
                if session == self:
                    del self.role_session_map[role][key]
                    break

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        if message_type == 'JOIN':
            # 处理 JOIN 类型的消息（如果需要广播，可以在这里实现）
            pass
        elif message_type == 'MESSAGE':
            # 处理 MESSAGE 类型的消息
            src_user_id = data.get('srcUserId')
            src_user_nickname = data.get('srcUserNicheng')
            to_role = data.get('toRole')
            target_user_id = data.get('targetUserId')
            msg = data.get('msg')

            if target_user_id:
                # 保存消息到数据库
                await self.save_message(src_user_id, src_user_nickname, target_user_id, msg)

                # 发送消息给目标用户
                await self.send_message_to_user(target_user_id, {
                    'type': 'MESSAGE',
                    'srcUserIdStr': src_user_id,
                    'srcUserNichengStr': src_user_nickname,
                    'msg': msg,
                    'sendTime': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
                })

    @database_sync_to_async
    def save_message(self, sender_id, sender_name, receiver_id, message):
        # 保存消息到数据库
        Consultation.objects.create(
            sender=sender_id,
            sender_name=sender_name,
            receiver=receiver_id,
            msg=message,
            send_time=timezone.now(),
            read_status=0
        )

    async def send_message_to_user(self, target_user_id, message):
        # 查找目标用户的会话并发送消息
        for role, user_sessions in self.role_session_map.items():
            for (user_id, nickname), session in user_sessions.items():
                if user_id == target_user_id:
                    await session.send(text_data=json.dumps(message))
                    break

class LetterWebSocketConsumer(AsyncWebsocketConsumer):
    # 存储用户会话的字典
    session_map = {}

    async def connect(self):
        # 获取 URL 参数
        query_params = self.scope['query_string'].decode('utf-8')
        params = {k: v for k, v in [param.split('=') for param in query_params.split('&')]}
        user_id = int(params.get('userId'))
        nickname = params.get('nicheng')

        # 将用户会话存储到字典中
        self.session_map[(user_id, nickname)] = self

        # 接受 WebSocket 连接
        await self.accept()

    async def disconnect(self, close_code):
        # 从字典中移除用户会话
        for key, session in self.session_map.items():
            if session == self:
                del self.session_map[key]
                break

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        if message_type == 'JOIN':
            # 处理 JOIN 类型的消息（如果需要广播，可以在这里实现）
            pass
        elif message_type == 'MESSAGE':
            # 处理 MESSAGE 类型的消息
            src_user_id = data.get('srcUserId')
            src_user_nickname = data.get('srcUserNicheng')
            target_user_id = data.get('targetUserId')
            msg = data.get('msg')

            if target_user_id:
                # 保存消息到数据库
                await self.save_message(src_user_id, src_user_nickname, target_user_id, msg)

                # 发送消息给目标用户
                await self.send_message_to_user(target_user_id, {
                    'type': 'MESSAGE',
                    'srcUserIdStr': src_user_id,
                    'srcUserNichengStr': src_user_nickname,
                    'msg': msg,
                    'sendTime': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
                })

    @database_sync_to_async
    def save_message(self, sender_id, sender_name, receiver_id, message):
        # 保存消息到数据库
        Letter.objects.create(
            sender=sender_id,
            sender_name=sender_name,
            receiver=receiver_id,
            msg=message,
            send_time=timezone.now(),
            read_status=0
        )

    async def send_message_to_user(self, target_user_id, message):
        # 查找目标用户的会话并发送消息
        for (user_id, nickname), session in self.session_map.items():
            if user_id == target_user_id:
                await session.send(text_data=json.dumps(message))
                break