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
from storeup.models import Storeup


# 保存
class KechengziyuanxinxiSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            kechengmingcheng=data['kechengmingcheng']
            if kechengmingcheng == '':
                kechengmingcheng = None
        except KeyError:
            kechengmingcheng = None
        except ValueError:
            kechengmingcheng = None
        try:
            tupian=data['tupian']
            if tupian == '':
                tupian = None
        except KeyError:
            tupian = None
        except ValueError:
            tupian = None
        try:
            kechengleixing=data['kechengleixing']
            if kechengleixing == '':
                kechengleixing = None
        except KeyError:
            kechengleixing = None
        except ValueError:
            kechengleixing = None
        try:
            kechengshipin=data['kechengshipin']
            if kechengshipin == '':
                kechengshipin = None
        except KeyError:
            kechengshipin = None
        except ValueError:
            kechengshipin = None
        try:
            fujian=data['fujian']
            if fujian == '':
                fujian = None
        except KeyError:
            fujian = None
        except ValueError:
            fujian = None
        try:
            shangchuanshijian=data['shangchuanshijian']
            if shangchuanshijian == '':
                shangchuanshijian = None
        except KeyError:
            shangchuanshijian = None
        except ValueError:
            shangchuanshijian = None
        try:
            beizhu=data['beizhu']
            if beizhu == '':
                beizhu = None
        except KeyError:
            beizhu = None
        except ValueError:
            beizhu = None
        try:
            xiangqing=data['xiangqing']
            if xiangqing == '':
                xiangqing = None
        except KeyError:
            xiangqing = None
        except ValueError:
            xiangqing = None
        try:
            sfsh=data['sfsh']
            if sfsh == '':
                sfsh = None
        except KeyError:
            sfsh = None
        except ValueError:
            sfsh = None
        try:
            shhf=data['shhf']
            if shhf == '':
                shhf = None
        except KeyError:
            shhf = None
        except ValueError:
            shhf = None
        Kechengziyuanxinxi.objects.create(
            kechengmingcheng=kechengmingcheng,
            tupian=tupian,
            kechengleixing=kechengleixing,
            kechengshipin=kechengshipin,
            fujian=fujian,
            shangchuanshijian=shangchuanshijian,
            beizhu=beizhu,
            xiangqing=xiangqing,
            sfsh=sfsh,
            shhf=shhf,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class KechengziyuanxinxiUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        kechengmingcheng=data['kechengmingcheng']
        tupian=data['tupian']
        kechengleixing=data['kechengleixing']
        kechengshipin=data['kechengshipin']
        fujian=data['fujian']
        shangchuanshijian=data['shangchuanshijian']
        beizhu=data['beizhu']
        xiangqing=data['xiangqing']
        sfsh=data['sfsh']
        shhf=data['shhf']
        id = data['id']
        Kechengziyuanxinxi.objects.filter(id=id).update(
        id=id,
        kechengmingcheng=kechengmingcheng,
        tupian=tupian,
        kechengleixing=kechengleixing,
        kechengshipin=kechengshipin,
        fujian=fujian,
        shangchuanshijian=shangchuanshijian,
        beizhu=beizhu,
        xiangqing=xiangqing,
        sfsh=sfsh,
        shhf=shhf,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class KechengziyuanxinxiDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Kechengziyuanxinxi.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class KechengziyuanxinxiInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Kechengziyuanxinxi.objects.filter(id=int(id)).all()
        entityser = KechengziyuanxinxiSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class KechengziyuanxinxiList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return KechengziyuanxinxiListNotPage(request)
        else:
            return KechengziyuanxinxiListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return KechengziyuanxinxiListNotPage(request)
        else:
            return KechengziyuanxinxiListPage(request)

def KechengziyuanxinxiListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'kechengmingcheng__icontains': request.query_params.get('kechengmingcheng'),
                                'tupian__icontains': request.query_params.get('tupian'),
                                'kechengleixing__icontains': request.query_params.get('kechengleixing'),
                                'kechengshipin__icontains': request.query_params.get('kechengshipin'),
                                'fujian__icontains': request.query_params.get('fujian'),
                                'shangchuanshijian__icontains': request.query_params.get('shangchuanshijian'),
                                'beizhu__icontains': request.query_params.get('beizhu'),
                                'xiangqing__icontains': request.query_params.get('xiangqing'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Kechengziyuanxinxi.objects.filter(q_objects).all()
    count = Kechengziyuanxinxi.objects.filter(q_objects).count()

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
    result = KechengziyuanxinxiSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def KechengziyuanxinxiListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'kechengmingcheng__icontains': request.query_params.get('kechengmingcheng'),
                                'tupian__icontains': request.query_params.get('tupian'),
                                'kechengleixing__icontains': request.query_params.get('kechengleixing'),
                                'kechengshipin__icontains': request.query_params.get('kechengshipin'),
                                'fujian__icontains': request.query_params.get('fujian'),
                                'shangchuanshijian__icontains': request.query_params.get('shangchuanshijian'),
                                'beizhu__icontains': request.query_params.get('beizhu'),
                                'xiangqing__icontains': request.query_params.get('xiangqing'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Kechengziyuanxinxi.objects.filter(q_objects).all()
    count = Kechengziyuanxinxi.objects.filter(q_objects).count()
    result = KechengziyuanxinxiSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class KechengziyuanxinxiPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'kechengmingcheng__icontains': request.query_params.get('kechengmingcheng'),
            'tupian__icontains': request.query_params.get('tupian'),
            'kechengleixing__icontains': request.query_params.get('kechengleixing'),
            'kechengshipin__icontains': request.query_params.get('kechengshipin'),
            'fujian__icontains': request.query_params.get('fujian'),
            'shangchuanshijian__icontains': request.query_params.get('shangchuanshijian'),
            'beizhu__icontains': request.query_params.get('beizhu'),
            'xiangqing__icontains': request.query_params.get('xiangqing'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Kechengziyuanxinxi.objects.filter(q_objects).all()
        count = Kechengziyuanxinxi.objects.filter(q_objects).count()

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
        result = KechengziyuanxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'kechengmingcheng__icontains': request.query_params.get('kechengmingcheng'),
            'tupian__icontains': request.query_params.get('tupian'),
            'kechengleixing__icontains': request.query_params.get('kechengleixing'),
            'kechengshipin__icontains': request.query_params.get('kechengshipin'),
            'fujian__icontains': request.query_params.get('fujian'),
            'shangchuanshijian__icontains': request.query_params.get('shangchuanshijian'),
            'beizhu__icontains': request.query_params.get('beizhu'),
            'xiangqing__icontains': request.query_params.get('xiangqing'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Kechengziyuanxinxi.objects.filter(q_objects).all()
        count = Kechengziyuanxinxi.objects.filter(q_objects).count()

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
        result = KechengziyuanxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})


# 推荐
class Recommend(APIView):
    def post(self, request):
        user_id = request.query_params.get('userId')
        num = request.query_params.get('num')

        # 使用 values_list 获取每个用户及其对应的收藏id
        queryset = Storeup.objects.values_list('userid', 'refid')
        
        # 使用 defaultdict 来方便地构建 Dict[userid, Set[refid]] 结构
        collections = defaultdict(set)
        
        for userid, refid in queryset:
            collections[str(userid)].add(refid)
        
        # 将 defaultdict 转换为普通的 dict
        user_item_collections = dict(collections)
        # 查询数据库，将Dict传入UserBasedCollaborativeFiltering
        userBasedCF = UserBasedCollaborativeFiltering(user_item_collections)
        recommendations = userBasedCF.recommend_items(user_id, num)
        keys = recommendations.keys()
        # 使用 Django ORM
        recommended_items = Kechengziyuanxinxi.objects.filter(id__in=keys)
        result = [Kechengziyuanxinxi.kechengziyuanxinxi_to_dict(item) for item in recommended_items]
        return Response({'code': 0, 'data': result})






def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

