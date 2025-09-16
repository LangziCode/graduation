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
class OrdersSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            orderid=data['orderid']
            if orderid == '':
                orderid = None
        except KeyError:
            orderid = None
        except ValueError:
            orderid = None
        try:
            tablename=data['tablename']
            if tablename == '':
                tablename = None
        except KeyError:
            tablename = None
        except ValueError:
            tablename = None
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        try:
            goodid=data['goodid']
            if goodid == '':
                goodid = None
        except KeyError:
            goodid = None
        except ValueError:
            goodid = None
        try:
            goodname=data['goodname']
            if goodname == '':
                goodname = None
        except KeyError:
            goodname = None
        except ValueError:
            goodname = None
        try:
            picture=data['picture']
            if picture == '':
                picture = None
        except KeyError:
            picture = None
        except ValueError:
            picture = None
        try:
            buynumber=data['buynumber']
            if buynumber == '':
                buynumber = None
        except KeyError:
            buynumber = None
        except ValueError:
            buynumber = None
        try:
            price=data['price']
            if price == '':
                price = None
        except KeyError:
            price = None
        except ValueError:
            price = None
        try:
            discountprice=data['discountprice']
            if discountprice == '':
                discountprice = None
        except KeyError:
            discountprice = None
        except ValueError:
            discountprice = None
        try:
            total=data['total']
            if total == '':
                total = None
        except KeyError:
            total = None
        except ValueError:
            total = None
        try:
            discounttotal=data['discounttotal']
            if discounttotal == '':
                discounttotal = None
        except KeyError:
            discounttotal = None
        except ValueError:
            discounttotal = None
        try:
            type=data['type']
            if type == '':
                type = None
        except KeyError:
            type = None
        except ValueError:
            type = None
        try:
            status=data['status']
            if status == '':
                status = None
        except KeyError:
            status = None
        except ValueError:
            status = None
        try:
            address=data['address']
            if address == '':
                address = None
        except KeyError:
            address = None
        except ValueError:
            address = None
        Orders.objects.create(
            orderid=orderid,
            tablename=tablename,
            userid=userid,
            goodid=goodid,
            goodname=goodname,
            picture=picture,
            buynumber=buynumber,
            price=price,
            discountprice=discountprice,
            total=total,
            discounttotal=discounttotal,
            type=type,
            status=status,
            address=address,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class OrdersUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        orderid=data['orderid']
        tablename=data['tablename']
        userid=data['userid']
        goodid=data['goodid']
        goodname=data['goodname']
        picture=data['picture']
        buynumber=data['buynumber']
        price=data['price']
        discountprice=data['discountprice']
        total=data['total']
        discounttotal=data['discounttotal']
        type=data['type']
        status=data['status']
        address=data['address']
        id = data['id']
        Orders.objects.filter(id=id).update(
        id=id,
        orderid=orderid,
        tablename=tablename,
        userid=userid,
        goodid=goodid,
        goodname=goodname,
        picture=picture,
        buynumber=buynumber,
        price=price,
        discountprice=discountprice,
        total=total,
        discounttotal=discounttotal,
        type=type,
        status=status,
        address=address,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class OrdersDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Orders.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class OrdersInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Orders.objects.filter(id=int(id)).all()
        entityser = OrdersSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class OrdersList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return OrdersListNotPage(request)
        else:
            return OrdersListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return OrdersListNotPage(request)
        else:
            return OrdersListPage(request)

def OrdersListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'orderid__icontains': request.query_params.get('orderid'),
                                'tablename__icontains': request.query_params.get('tablename'),
                                                'goodid__icontains': request.query_params.get('goodid'),
                                'goodname__icontains': request.query_params.get('goodname'),
                                'picture__icontains': request.query_params.get('picture'),
                                'buynumber__icontains': request.query_params.get('buynumber'),
                                'price__icontains': request.query_params.get('price'),
                                'discountprice__icontains': request.query_params.get('discountprice'),
                                'total__icontains': request.query_params.get('total'),
                                'discounttotal__icontains': request.query_params.get('discounttotal'),
                                'type__icontains': request.query_params.get('type'),
                                'status__icontains': request.query_params.get('status'),
                                'address__icontains': request.query_params.get('address'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Orders.objects.filter(q_objects).all()
    count = Orders.objects.filter(q_objects).count()

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
    result = OrdersSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def OrdersListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'orderid__icontains': request.query_params.get('orderid'),
                                'tablename__icontains': request.query_params.get('tablename'),
                                                'goodid__icontains': request.query_params.get('goodid'),
                                'goodname__icontains': request.query_params.get('goodname'),
                                'picture__icontains': request.query_params.get('picture'),
                                'buynumber__icontains': request.query_params.get('buynumber'),
                                'price__icontains': request.query_params.get('price'),
                                'discountprice__icontains': request.query_params.get('discountprice'),
                                'total__icontains': request.query_params.get('total'),
                                'discounttotal__icontains': request.query_params.get('discounttotal'),
                                'type__icontains': request.query_params.get('type'),
                                'status__icontains': request.query_params.get('status'),
                                'address__icontains': request.query_params.get('address'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Orders.objects.filter(q_objects).all()
    count = Orders.objects.filter(q_objects).count()
    result = OrdersSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class OrdersPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'orderid__icontains': request.query_params.get('orderid'),
            'tablename__icontains': request.query_params.get('tablename'),
            'userid__icontains': request.query_params.get('userid'),
            'goodid__icontains': request.query_params.get('goodid'),
            'goodname__icontains': request.query_params.get('goodname'),
            'picture__icontains': request.query_params.get('picture'),
            'buynumber__icontains': request.query_params.get('buynumber'),
            'price__icontains': request.query_params.get('price'),
            'discountprice__icontains': request.query_params.get('discountprice'),
            'total__icontains': request.query_params.get('total'),
            'discounttotal__icontains': request.query_params.get('discounttotal'),
            'type__icontains': request.query_params.get('type'),
            'status__icontains': request.query_params.get('status'),
            'address__icontains': request.query_params.get('address'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Orders.objects.filter(q_objects).all()
        count = Orders.objects.filter(q_objects).count()

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
        result = OrdersSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'orderid__icontains': request.query_params.get('orderid'),
            'tablename__icontains': request.query_params.get('tablename'),
            'userid__icontains': request.query_params.get('userid'),
            'goodid__icontains': request.query_params.get('goodid'),
            'goodname__icontains': request.query_params.get('goodname'),
            'picture__icontains': request.query_params.get('picture'),
            'buynumber__icontains': request.query_params.get('buynumber'),
            'price__icontains': request.query_params.get('price'),
            'discountprice__icontains': request.query_params.get('discountprice'),
            'total__icontains': request.query_params.get('total'),
            'discounttotal__icontains': request.query_params.get('discounttotal'),
            'type__icontains': request.query_params.get('type'),
            'status__icontains': request.query_params.get('status'),
            'address__icontains': request.query_params.get('address'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Orders.objects.filter(q_objects).all()
        count = Orders.objects.filter(q_objects).count()

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
        result = OrdersSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

