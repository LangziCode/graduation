from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from forum.serializers import *
from utils.myjwt import myjwt

class Save(APIView):
    def post(self, request):
        data = request.data
        try:
            title = data['title']
        except KeyError:
            title = None
        content = data['content']
        if 'parentid' in data:
            parentid = data['parentid']
        else:
            parentid = 0
        username = data['username']
        try:
            isdone = data['isdone']
        except KeyError:
            isdone = None
        # userid = request.session.get('users')
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
    
        Forum.objects.create(
            title=title,
            content=content,
            parentid=parentid,
            userid=userid,
            username=username,
            isdone=isdone
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
        title = request.query_params.get('title')
        if title:
            queryset = Forum.objects.filter(title__icontains=title[1:-1]).all()
            count = Forum.objects.filter(title__icontains=title[1:-1]).count()
        else:
            queryset = Forum.objects.all()
            count = Forum.objects.count()
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
        yonghulies = ForumSer(items, many=True)
        return Response({'code': 0, 'data': {'list': yonghulies.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        try:
            limit = request.query_params.get('limit')  # 数量
            if limit is None:
                limit = 10
        except Exception as e:
            limit = 10
        title = request.query_params.get('title')
        if title:
            queryset = Forum.objects.filter(title__icontains=title[1:-1]).all()
            count = Forum.objects.filter(title__icontains=title[1:-1]).count()
        else:
            queryset = Forum.objects.all()
            count = Forum.objects.count()
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
        yonghulies = ForumSer(items, many=True)
        return Response({'code': 0, 'data': {'list': yonghulies.data, 'total': count}})
        
class List(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        queryset = Forum.objects.filter(parentid=0).all()
        count = Forum.objects.filter(parentid=0).count()
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
        result = ForumSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        queryset = Forum.objects.filter(parentid=0).all()
        count = Forum.objects.filter(parentid=0).count()
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
        result = ForumSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})


class ForumDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            forumid = id
            Forum.objects.filter(id=int(forumid)).delete()
        # 尝试从请求数据中获取论坛ID列表
        return Response({'code': 0, 'msg': '删除成功'})


class ForumUpdate(APIView):
    def post(self, request):
        data = request.data
        forumid = data['id']
        title = data['title']
        content = data['content']
        parentid = data['parentid']
        userid = data['userid']
        username = data['username']
        isdone = data['isdone']
        print(id, type(id))
        Forum.objects.filter(id=int(forumid)).update(
            title=title,
            content=content,
            parentid=parentid,
            userid=userid,
            username=username,
            isdone=isdone
        )
        return Response({'code': 0, 'msg': '修改成功'})


class Info(APIView):
    def get(self, request, id):
        a = Forum.objects.filter(id=int(id)).all()
        lista = ForumSer(a, many=True)
        return Response({'code': 0, 'data': lista.data[0]})
        
class ListInfo(APIView):
    def get(self, request, id):
        forum = Forum.objects.filter(id=int(id)).all()
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
    child_list = Forum.objects.filter(parentid=int(id)).all()
    child_list = ForumSer(child_list, many=True)
    return child_list.data
