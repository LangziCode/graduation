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

class GroupBy(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        token_info = Token.objects.get(token=token)
        userid = myjwt.jwt_decode(token)['data']['userid']
        if token_info.role != '管理员':
            # 查询数据
            queryset = Examrecord.objects.filter(userid=userid).values('userid', 'username', 'paperid', 'papername').annotate(myscore=Sum('myscore'))
        else:
            # 查询数据
            queryset = Examrecord.objects.filter().values('userid', 'username', 'paperid', 'papername').annotate(myscore=Sum('myscore'))
        count = queryset.count()
        # 设置每页显示的记录数
        paginator = Paginator(queryset, limit)  # 每页显示 10 条记录
        # 获取当前页码
        page_number = request.GET.get('page', page)
        # 获取当前页的分页对象
        page_obj = paginator.get_page(page_number)
        result = ExamrecordSer(page_obj, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})


class DeleteRecords(APIView):
    def post(self, request):
        userid = request.query_params.get('userid')
        paperid = request.query_params.get('paperid')
        Examrecord.objects.filter(userid=userid, paperid=paperid).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 保存
class ExamrecordSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        try:
            username=data['username']
            if username == '':
                username = None
        except KeyError:
            username = None
        except ValueError:
            username = None
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
            questionid=data['questionid']
            if questionid == '':
                questionid = None
        except KeyError:
            questionid = None
        except ValueError:
            questionid = None
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
            myscore=data['myscore']
            if myscore == '':
                myscore = None
        except KeyError:
            myscore = None
        except ValueError:
            myscore = None
        try:
            myanswer=data['myanswer']
            if myanswer == '':
                myanswer = None
        except KeyError:
            myanswer = None
        except ValueError:
            myanswer = None
        Examrecord.objects.create(
            userid=userid,
            username=username,
            paperid=paperid,
            papername=papername,
            questionid=questionid,
            questionname=questionname,
            options=options,
            score=score,
            answer=answer,
            analysis=analysis,
            myscore=myscore,
            myanswer=myanswer,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class ExamrecordUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        userid=data['userid']
        username=data['username']
        paperid=data['paperid']
        papername=data['papername']
        questionid=data['questionid']
        questionname=data['questionname']
        options=data['options']
        score=data['score']
        answer=data['answer']
        analysis=data['analysis']
        myscore=data['myscore']
        myanswer=data['myanswer']
        id = data['id']
        Examrecord.objects.filter(id=id).update(
        id=id,
        userid=userid,
        username=username,
        paperid=paperid,
        papername=papername,
        questionid=questionid,
        questionname=questionname,
        options=options,
        score=score,
        answer=answer,
        analysis=analysis,
        myscore=myscore,
        myanswer=myanswer,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class ExamrecordDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Examrecord.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class ExamrecordInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Examrecord.objects.filter(id=int(id)).all()
        entityser = ExamrecordSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class ExamrecordList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return ExamrecordListNotPage(request)
        else:
            return ExamrecordListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return ExamrecordListNotPage(request)
        else:
            return ExamrecordListPage(request)

def ExamrecordListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                                'username__icontains': request.query_params.get('username'),
                                'paperid__icontains': request.query_params.get('paperid'),
                                'papername__icontains': request.query_params.get('papername'),
                                'questionid__icontains': request.query_params.get('questionid'),
                                'questionname__icontains': request.query_params.get('questionname'),
                                'options__icontains': request.query_params.get('options'),
                                'score__icontains': request.query_params.get('score'),
                                'answer__icontains': request.query_params.get('answer'),
                                'analysis__icontains': request.query_params.get('analysis'),
                                'myscore__icontains': request.query_params.get('myscore'),
                                'myanswer__icontains': request.query_params.get('myanswer'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Examrecord.objects.filter(q_objects).all()
    count = Examrecord.objects.filter(q_objects).count()

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
    result = ExamrecordSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def ExamrecordListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                                'username__icontains': request.query_params.get('username'),
                                'paperid__icontains': request.query_params.get('paperid'),
                                'papername__icontains': request.query_params.get('papername'),
                                'questionid__icontains': request.query_params.get('questionid'),
                                'questionname__icontains': request.query_params.get('questionname'),
                                'options__icontains': request.query_params.get('options'),
                                'score__icontains': request.query_params.get('score'),
                                'answer__icontains': request.query_params.get('answer'),
                                'analysis__icontains': request.query_params.get('analysis'),
                                'myscore__icontains': request.query_params.get('myscore'),
                                'myanswer__icontains': request.query_params.get('myanswer'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Examrecord.objects.filter(q_objects).all()
    count = Examrecord.objects.filter(q_objects).count()
    result = ExamrecordSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class ExamrecordPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'userid__icontains': request.query_params.get('userid'),
            'username__icontains': request.query_params.get('username'),
            'paperid__icontains': request.query_params.get('paperid'),
            'papername__icontains': request.query_params.get('papername'),
            'questionid__icontains': request.query_params.get('questionid'),
            'questionname__icontains': request.query_params.get('questionname'),
            'options__icontains': request.query_params.get('options'),
            'score__icontains': request.query_params.get('score'),
            'answer__icontains': request.query_params.get('answer'),
            'analysis__icontains': request.query_params.get('analysis'),
            'myscore__icontains': request.query_params.get('myscore'),
            'myanswer__icontains': request.query_params.get('myanswer'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Examrecord.objects.filter(q_objects).all()
        count = Examrecord.objects.filter(q_objects).count()

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
        result = ExamrecordSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'userid__icontains': request.query_params.get('userid'),
            'username__icontains': request.query_params.get('username'),
            'paperid__icontains': request.query_params.get('paperid'),
            'papername__icontains': request.query_params.get('papername'),
            'questionid__icontains': request.query_params.get('questionid'),
            'questionname__icontains': request.query_params.get('questionname'),
            'options__icontains': request.query_params.get('options'),
            'score__icontains': request.query_params.get('score'),
            'answer__icontains': request.query_params.get('answer'),
            'analysis__icontains': request.query_params.get('analysis'),
            'myscore__icontains': request.query_params.get('myscore'),
            'myanswer__icontains': request.query_params.get('myanswer'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Examrecord.objects.filter(q_objects).all()
        count = Examrecord.objects.filter(q_objects).count()

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
        result = ExamrecordSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

