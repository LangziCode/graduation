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
class ExamquestionSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            paperid=data['paperid']
            if paperid == '':
                paperid = None
        except KeyError:
            paperid = None
        except ValueError:
            paperid = None
        try:
            papername=data['papername']
            if papername == '':
                papername = None
        except KeyError:
            papername = None
        except ValueError:
            papername = None
        try:
            questionname=data['questionname']
            if questionname == '':
                questionname = None
        except KeyError:
            questionname = None
        except ValueError:
            questionname = None
        try:
            options=data['options']
            if options == '':
                options = None
        except KeyError:
            options = None
        except ValueError:
            options = None
        try:
            score=data['score']
            if score == '':
                score = None
        except KeyError:
            score = None
        except ValueError:
            score = None
        try:
            answer=data['answer']
            if answer == '':
                answer = None
        except KeyError:
            answer = None
        except ValueError:
            answer = None
        try:
            analysis=data['analysis']
            if analysis == '':
                analysis = None
        except KeyError:
            analysis = None
        except ValueError:
            analysis = None
        try:
            type=data['type']
            if type == '':
                type = None
        except KeyError:
            type = None
        except ValueError:
            type = None
        try:
            sequence=data['sequence']
            if sequence == '':
                sequence = None
        except KeyError:
            sequence = None
        except ValueError:
            sequence = None
        Examquestion.objects.create(
            paperid=paperid,
            papername=papername,
            questionname=questionname,
            options=options,
            score=score,
            answer=answer,
            analysis=analysis,
            type=type,
            sequence=sequence,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class ExamquestionUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        paperid=data['paperid']
        papername=data['papername']
        questionname=data['questionname']
        options=data['options']
        score=data['score']
        answer=data['answer']
        analysis=data['analysis']
        type=data['type']
        sequence=data['sequence']
        id = data['id']
        Examquestion.objects.filter(id=id).update(
        id=id,
        paperid=paperid,
        papername=papername,
        questionname=questionname,
        options=options,
        score=score,
        answer=answer,
        analysis=analysis,
        type=type,
        sequence=sequence,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class ExamquestionDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Examquestion.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class ExamquestionInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Examquestion.objects.filter(id=int(id)).all()
        entityser = ExamquestionSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class ExamquestionList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return ExamquestionListNotPage(request)
        else:
            return ExamquestionListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return ExamquestionListNotPage(request)
        else:
            return ExamquestionListPage(request)

def ExamquestionListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'paperid__icontains': request.query_params.get('paperid'),
                                'papername__icontains': request.query_params.get('papername'),
                                'questionname__icontains': request.query_params.get('questionname'),
                                'options__icontains': request.query_params.get('options'),
                                'score__icontains': request.query_params.get('score'),
                                'answer__icontains': request.query_params.get('answer'),
                                'analysis__icontains': request.query_params.get('analysis'),
                                'type__icontains': request.query_params.get('type'),
                                'sequence__icontains': request.query_params.get('sequence'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Examquestion.objects.filter(q_objects).all()
    count = Examquestion.objects.filter(q_objects).count()

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
    result = ExamquestionSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def ExamquestionListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'paperid__icontains': request.query_params.get('paperid'),
                                'papername__icontains': request.query_params.get('papername'),
                                'questionname__icontains': request.query_params.get('questionname'),
                                'options__icontains': request.query_params.get('options'),
                                'score__icontains': request.query_params.get('score'),
                                'answer__icontains': request.query_params.get('answer'),
                                'analysis__icontains': request.query_params.get('analysis'),
                                'type__icontains': request.query_params.get('type'),
                                'sequence__icontains': request.query_params.get('sequence'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Examquestion.objects.filter(q_objects).all()
    count = Examquestion.objects.filter(q_objects).count()
    result = ExamquestionSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class ExamquestionPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'paperid__icontains': request.query_params.get('paperid'),
            'papername__icontains': request.query_params.get('papername'),
            'questionname__icontains': request.query_params.get('questionname'),
            'options__icontains': request.query_params.get('options'),
            'score__icontains': request.query_params.get('score'),
            'answer__icontains': request.query_params.get('answer'),
            'analysis__icontains': request.query_params.get('analysis'),
            'type__icontains': request.query_params.get('type'),
            'sequence__icontains': request.query_params.get('sequence'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Examquestion.objects.filter(q_objects).all()
        count = Examquestion.objects.filter(q_objects).count()

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
        result = ExamquestionSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'paperid__icontains': request.query_params.get('paperid'),
            'papername__icontains': request.query_params.get('papername'),
            'questionname__icontains': request.query_params.get('questionname'),
            'options__icontains': request.query_params.get('options'),
            'score__icontains': request.query_params.get('score'),
            'answer__icontains': request.query_params.get('answer'),
            'analysis__icontains': request.query_params.get('analysis'),
            'type__icontains': request.query_params.get('type'),
            'sequence__icontains': request.query_params.get('sequence'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Examquestion.objects.filter(q_objects).all()
        count = Examquestion.objects.filter(q_objects).count()

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
        result = ExamquestionSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

