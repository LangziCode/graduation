import re
from django.db.models import Q, Value, F
from rest_framework.views import APIView
from rest_framework.response import Response



import time
import random
import datetime
from datetime import timedelta
from utils.myjwt import myjwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from address.models import *
from address.serializers import *
from orders.models import *
from orders.serializers import *
from cart.models import *
from cart.serializers import *
from news.models import *
from news.serializers import *
from messagess.models import *
from messagess.serializers import *
from exampaper.models import *
from exampaper.serializers import *
from examquestion.models import *
from examquestion.serializers import *
from examrecord.models import *
from examrecord.serializers import *
from kechengxinxi.models import *
from kechengxinxi.serializers import *
from discusskechengxinxi.models import *
from discusskechengxinxi.serializers import *
from kechengziyuanxinxi.models import *
from kechengziyuanxinxi.serializers import *
from discusskechengziyuanxinxi.models import *
from discusskechengziyuanxinxi.serializers import *
from kechengleixing.models import *
from kechengleixing.serializers import *
from xuexijihua.models import *
from xuexijihua.serializers import *
from jiaoshi.models import *
from jiaoshi.serializers import *
from xuesheng.models import *
from xuesheng.serializers import *
from tokens.models import *
from utils import *
from collections import defaultdict


# 保存
class JiaoshiSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            yonghuming=data['yonghuming']
            if yonghuming == '':
                yonghuming = None
        except KeyError:
            yonghuming = None
        except ValueError:
            yonghuming = None
        try:
            mima=data['mima']
            if mima == '':
                mima = None
        except KeyError:
            mima = None
        except ValueError:
            mima = None
        try:
            xingbie=data['xingbie']
            if xingbie == '':
                xingbie = None
        except KeyError:
            xingbie = None
        except ValueError:
            xingbie = None
        try:
            dianhua=data['dianhua']
            if dianhua == '':
                dianhua = None
        except KeyError:
            dianhua = None
        except ValueError:
            dianhua = None
        try:
            nicheng=data['nicheng']
            if nicheng == '':
                nicheng = None
        except KeyError:
            nicheng = None
        except ValueError:
            nicheng = None
        try:
            money=data['money']
            if money == '':
                money = None
        except KeyError:
            money = None
        except ValueError:
            money = None
        Jiaoshi.objects.create(
            yonghuming=yonghuming,
            mima=mima,
            xingbie=xingbie,
            dianhua=dianhua,
            nicheng=nicheng,
            money=money,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class JiaoshiUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        yonghuming=data['yonghuming']
        mima=data['mima']
        xingbie=data['xingbie']
        dianhua=data['dianhua']
        nicheng=data['nicheng']
        money=data['money']
        id = data['id']
        Jiaoshi.objects.filter(id=id).update(
        id=id,
        yonghuming=yonghuming,
        mima=mima,
        xingbie=xingbie,
        dianhua=dianhua,
        nicheng=nicheng,
        money=money,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class JiaoshiDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Jiaoshi.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class JiaoshiInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Jiaoshi.objects.filter(id=int(id)).all()
        entityser = JiaoshiSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class JiaoshiList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return JiaoshiListNotPage(request)
        else:
            return JiaoshiListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return JiaoshiListNotPage(request)
        else:
            return JiaoshiListPage(request)

def JiaoshiListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'mima__icontains': request.query_params.get('mima'),
                                'xingbie__icontains': request.query_params.get('xingbie'),
                                'dianhua__icontains': request.query_params.get('dianhua'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'money__icontains': request.query_params.get('money'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Jiaoshi.objects.filter(q_objects).all()
    count = Jiaoshi.objects.filter(q_objects).count()

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
    result = JiaoshiSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def JiaoshiListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'mima__icontains': request.query_params.get('mima'),
                                'xingbie__icontains': request.query_params.get('xingbie'),
                                'dianhua__icontains': request.query_params.get('dianhua'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'money__icontains': request.query_params.get('money'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Jiaoshi.objects.filter(q_objects).all()
    count = Jiaoshi.objects.filter(q_objects).count()
    result = JiaoshiSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class JiaoshiPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'mima__icontains': request.query_params.get('mima'),
            'xingbie__icontains': request.query_params.get('xingbie'),
            'dianhua__icontains': request.query_params.get('dianhua'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'money__icontains': request.query_params.get('money'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Jiaoshi.objects.filter(q_objects).all()
        count = Jiaoshi.objects.filter(q_objects).count()

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
            items = None
        result = JiaoshiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'mima__icontains': request.query_params.get('mima'),
            'xingbie__icontains': request.query_params.get('xingbie'),
            'dianhua__icontains': request.query_params.get('dianhua'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'money__icontains': request.query_params.get('money'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Jiaoshi.objects.filter(q_objects).all()
        count = Jiaoshi.objects.filter(q_objects).count()

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
        result = JiaoshiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})







# 用户登录
class LoginJiaoshi(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Jiaoshi.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='jiaoshi',
                role='教师',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Jiaoshi.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='jiaoshi',
                role='教师',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

# 用户获取session
class JiaoshiSession(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Jiaoshi.objects.filter(id=session).all()
        user_ser = JiaoshiSer(users, many=True)
        user_ser.data[0]['role'] = 'jiaoshi'
        return Response({'code': 0, 'data': user_ser.data[0]})

    def post(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Jiaoshi.objects.filter(id=session).all()
        user_ser = JiaoshiSer(users, many=True)
        user_ser.data[0]['role'] = 'jiaoshi'
        return Response({'code': 0, 'data': user_ser.data[0]})

# 用户注册
class Register(APIView):
    def post(self, request):
        data = request.data
        yonghuming=data['yonghuming']
        mima=data['mima']
        xingbie=data['xingbie']
        dianhua=data['dianhua']
        nicheng=data['nicheng']
        if not all([
        yonghuming,
        mima,
        xingbie,
        dianhua,
        nicheng,
    ]):
            return Response({"code": 401, 'msg': '参数不全'})


        Jiaoshi.objects.create(
            id=generate_unique_userid(),
            yonghuming=yonghuming,
            mima=mima,
            xingbie=xingbie,
            dianhua=dianhua,
            nicheng=nicheng,
        )
        return Response({'code': 0, 'msg': '注册成功'})
   



def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

