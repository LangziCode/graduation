from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from storeup.serializers import *
from utils.myjwt import myjwt

class Save(APIView):
    def post(self, request):
        data = request.data
        try:
            refid = data['refid']
        except KeyError:
            refid = None
        tablename = data['tablename']
        try:
            name = data['name']
        except KeyError:
            name = ''
        picture = data['picture']
        try:
            type = data['type']
        except KeyError:
            type = None
        # userid = request.session.get('users')
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        
        # addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
        # userid = models.IntegerField(verbose_name='用户id')
        # refid = models.IntegerField(verbose_name='收藏id')
        # tablename = models.CharField(max_length=200, verbose_name='表名')
        # name = models.CharField(max_length=200, verbose_name='收藏名称')
        # picture = models.CharField(max_length=200, verbose_name='收藏图片')
        # type = models.CharField(max_length=200, verbose_name='类型(1:收藏,21:赞,22:踩)')

        Storeup.objects.create(
            userid=userid,
            refid=refid,
            tablename=tablename,
            name=name,
            picture=picture,
            type='1'
        )
        return Response({"code": 0, 'msg': '添加成功'})

class Page(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        try:
            limit = request.query_params.get('limit')  # 数量
            if limit is None:
                limit = 10
        except Exception as e:
            limit = 10
        type = request.query_params.get('type')  # 类型
        sort = request.query_params.get('sort')  # 排序
        
        # userid = request.session.get('users')
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        
        if(type is None and sort is None):
            queryset = Storeup.objects.filter(userid=userid).all()
            count = Storeup.objects.filter(userid=userid).count()
        else:
            queryset = Storeup.objects.filter(type=type,userid=userid).order_by(sort).all()
            count = Storeup.objects.filter(type=type,userid=userid).count()
        # print(queryset)
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
        result = StoreupSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        try:
            limit = request.query_params.get('limit')  # 数量
            if limit is None:
                limit = 10
        except Exception as e:
            limit = 10
        type = request.query_params.get('type')  # 类型
        sort = request.query_params.get('sort')  # 排序

        # userid = request.session.get('users')
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']

        if (type is None and sort is None):
            queryset = Storeup.objects.filter(userid=userid).all()
            count = Storeup.objects.filter(userid=userid).count()
        else:
            queryset = Storeup.objects.filter(type=type, userid=userid).order_by(sort).all()
            count = Storeup.objects.filter(type=type, userid=userid).count()
        # print(queryset)
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
        result = StoreupSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})
        
class List(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        type = request.query_params.get('type')  # 类型
        refid = request.query_params.get('refid')
        
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        # userid = request.session.get('users')
        
        tablename = request.query_params.get('tablename')  # 表名
        if refid and tablename is None:
            queryset = Storeup.objects.filter(type=type, refid=refid, userid=userid).all()
            count = Storeup.objects.filter(type=type, refid=refid, userid=userid).count()
        elif refid and tablename:
            queryset = Storeup.objects.filter(type=type, refid=refid, tablename=tablename, userid=userid).all()
            count = Storeup.objects.filter(type=type, refid=refid, tablename=tablename, userid=userid).count()
        else:
            queryset = Storeup.objects.filter(type=type, userid=userid).all()
            count = Storeup.objects.filter(type=type, userid=userid).count()
        # print(queryset)
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
        result = StoreupSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        type = request.query_params.get('type')  # 类型
        refid = request.query_params.get('refid')

        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        # userid = request.session.get('users')

        tablename = request.query_params.get('tablename')  # 表名
        if refid and tablename is None:
            queryset = Storeup.objects.filter(type=type, refid=refid, userid=userid).all()
            count = Storeup.objects.filter(type=type, refid=refid, userid=userid).count()
        elif refid and tablename:
            queryset = Storeup.objects.filter(type=type, refid=refid, tablename=tablename, userid=userid).all()
            count = Storeup.objects.filter(type=type, refid=refid, tablename=tablename, userid=userid).count()
        else:
            queryset = Storeup.objects.filter(type=type, userid=userid).all()
            count = Storeup.objects.filter(type=type, userid=userid).count()
        # print(queryset)
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
        result = StoreupSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

class StoreupDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            storeupid = id
            Storeup.objects.filter(id=int(storeupid)).delete()
        # 尝试从请求数据中获取论坛ID列表
        return Response({'code': 0, 'msg': '删除成功'})


class StoreupUpdate(APIView):
    def post(self, request):
        data = request.data
        userid = data['userid']
        storeupid = data['id']
        refid = data['refid']
        tablename = data['tablename']
        name = data['name']
        picture = data['picture']
        type = data['type']
        Storeup.objects.filter(id=int(storeupid)).update(
            refid=refid,
            tablename=tablename,
            name=name,
            picture=picture,
            type=type
        )
        return Response({'code': 0, 'msg': '修改成功'})


class Info(APIView):
    def get(self, request, id):
        a = Storeup.objects.filter(id=int(id)).all()
        lista = StoreupSer(a, many=True)
        return Response({'code': 0, 'data': lista.data[0]})
        
class ListInfo(APIView):
    def get(self, request, id):
        forum = Storeup.objects.filter(id=int(id)).all()
        result = getChilds(forum[0])
        u = {}
        for i in forum:
            u['id'] = i.id
            u['addtime'] = i.addtime
            u['title'] = i.title
            u['content'] = i.content
            u['parentid'] = i.parentid
            u['userid'] = i.userid
            u['username'] = i.username
            u['isdone'] = i.isdone
        u['childs'] = result
        return Response({'code': 0, 'data': u})

def getChilds(forum):
    # 获取id
    id = forum.id
    # 通过帖子id查询评论
    child_list = Storeup.objects.filter(parentid=int(id)).all()
    child_list = StoreupSer(child_list, many=True)
    return child_list.data
