from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import time
import datetime
from datetime import timedelta
from users.serializers import *
from utils.myjwt import myjwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import *
from config.serializers import *

# Create your views here.


class Page(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        queryset = Config.objects.all()
        count = Config.objects.count()
        # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = paginator.page(paginator.num_pages)
        yonghulies = ConfigSer(items, many=True)
        return Response({'code': 0, 'data': {'list': yonghulies.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        queryset = Config.objects.all()
        count = Config.objects.count()
        # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = paginator.page(paginator.num_pages)
        yonghulies = ConfigSer(items, many=True)
        return Response({'code': 0, 'data': {'list': yonghulies.data, 'total': count}})
        
class List(APIView):
    def get(self, request):
        queryset = Config.objects.all()
        count = Config.objects.count()
        result = ConfigSer(queryset, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        queryset = Config.objects.all()
        count = Config.objects.count()
        result = ConfigSer(queryset, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

class Save(APIView):
    def post(self, request):
        data = request.data
        name = data['name']
        value = data['value']
        Config.objects.create(
            name=name,
            value=value
        )
        return Response({'code': 0, 'msg': '添加成功'})


class Info(APIView):
    def get(self, request, id):
        a = Config.objects.filter(id=int(id)).all()
        lista = ConfigSer(a, many=True)
        return Response({'code': 0, 'data': lista.data[0]})


class Update(APIView):
    def post(self, request):
        data = request.data
        id = data['id']
        name = data['name']
        value = data['value']
        Config.objects.filter(id=int(id)).update(
            name=name,
            value=value
        )
        return Response({'code': 0, 'msg': '修改成功'})


class Delete(APIView):
    def post(self, request):
        data = request.data
        id = data[0]
        Config.objects.filter(id=int(id)).delete()
        return Response({"code": 0, 'msg': '删除成功'})