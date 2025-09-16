from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import uuid

class Upload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')  # 从请求中获取图片文件
        if file:
            # 获取文件的扩展名
            file_ext = os.path.splitext(file.name)[1]
            # 生成唯一的文件名（使用 UUID）
            random_filename = f"{uuid.uuid4()}{file_ext}"
            # 定义文件存储路径
            file_path = os.path.join(settings.MEDIA_ROOT, 'media/upload/', random_filename)
            print('图片地址', file_path)
            # 确保存储目录存在
            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))
            # 保存文件到本地
            default_storage.save(file_path, ContentFile(file.read()))
            return Response({'code': 0, "file": random_filename})
        return Response({'code': 401, "msg": '上传失败'})

