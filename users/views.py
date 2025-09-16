from rest_framework.views import APIView
from rest_framework.response import Response
import time
import datetime
from datetime import timedelta
from .serializers import *
from utils.myjwt import myjwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tokens.models import *

# # 管理员登录
class LoginUsers(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        users = Users.objects.filter(username=username, password=password).first()
        if users:
            token = myjwt.jwt_encode({"data": {"userid": users.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(days=2)
            print(current_time, futue_time)
            print(current_time, futue_time)
            Token.objects.create(
                userid=users.id,
                username=users.username,
                tablename='users',
                role='管理员',
                token=token,
                addtime=current_time,
                expiratedtime=futue_time

            )
            request.session['users'] = users.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        users = Users.objects.filter(username=username, password=password).first()
        if users:
            token = myjwt.jwt_encode({"data": {"userid": users.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(days=2)
            print(current_time, futue_time)
            print(current_time, futue_time)
            Token.objects.create(
                userid=users.id,
                username=users.username,
                tablename='users',
                role='管理员',
                token=token,
                addtime=current_time,
                expiratedtime=futue_time

            )
            request.session['users'] = users.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})


# 管理员获取session
class UserSession(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        # session = request.session.get('users')
        users = Users.objects.filter(id=session).all()
        user_ser = UsersSer(users, many=True)
        return Response({'code': 0, 'data': user_ser.data[0]})

    def post(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        # session = request.session.get('users')
        users = Users.objects.filter(id=session).all()
        user_ser = UsersSer(users, many=True)
        return Response({'code': 0, 'data': user_ser.data[0]})


# 管理员信息更新
class UsersUpdate(APIView):
    def post(self, request):
        data = request.data
        print('data:', data)
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        # session = request.session.get('users')
        username = data['username']
        password = data['password']
        Users.objects.filter(id=session).update(
            username=username,
            password=password
        )
        return Response({'code': 0, 'msg': '修改成功'})