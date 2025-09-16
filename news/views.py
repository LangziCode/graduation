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
class NewsSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            title=data['title']
            if title == '':
                title = None
        except KeyError:
            title = None
        except ValueError:
            title = None
        try:
            introduction=data['introduction']
            if introduction == '':
                introduction = None
        except KeyError:
            introduction = None
        except ValueError:
            introduction = None
        try:
            picture=data['picture']
            if picture == '':
                picture = None
        except KeyError:
            picture = None
        except ValueError:
            picture = None
        try:
            content=data['content']
            if content == '':
                content = None
        except KeyError:
            content = None
        except ValueError:
            content = None
        News.objects.create(
            title=title,
            introduction=introduction,
            picture=picture,
            content=content,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class NewsUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        title=data['title']
        introduction=data['introduction']
        picture=data['picture']
        content=data['content']
        id = data['id']
        News.objects.filter(id=id).update(
        id=id,
        title=title,
        introduction=introduction,
        picture=picture,
        content=content,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class NewsDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            News.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class NewsInfo(APIView):
    def get(self, request, id):
        id = id
        entity = News.objects.filter(id=int(id)).all()
        entityser = NewsSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class NewsList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return NewsListNotPage(request)
        else:
            return NewsListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return NewsListNotPage(request)
        else:
            return NewsListPage(request)

def NewsListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'title__icontains': request.query_params.get('title'),
                                'introduction__icontains': request.query_params.get('introduction'),
                                'picture__icontains': request.query_params.get('picture'),
                                'content__icontains': request.query_params.get('content'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = News.objects.filter(q_objects).all()
    count = News.objects.filter(q_objects).count()

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
    result = NewsSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def NewsListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'title__icontains': request.query_params.get('title'),
                                'introduction__icontains': request.query_params.get('introduction'),
                                'picture__icontains': request.query_params.get('picture'),
                                'content__icontains': request.query_params.get('content'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = News.objects.filter(q_objects).all()
    count = News.objects.filter(q_objects).count()
    result = NewsSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class NewsPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'title__icontains': request.query_params.get('title'),
            'introduction__icontains': request.query_params.get('introduction'),
            'picture__icontains': request.query_params.get('picture'),
            'content__icontains': request.query_params.get('content'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = News.objects.filter(q_objects).all()
        count = News.objects.filter(q_objects).count()

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
        result = NewsSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'title__icontains': request.query_params.get('title'),
            'introduction__icontains': request.query_params.get('introduction'),
            'picture__icontains': request.query_params.get('picture'),
            'content__icontains': request.query_params.get('content'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = News.objects.filter(q_objects).all()
        count = News.objects.filter(q_objects).count()

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
        result = NewsSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

