from django.db.models import Count, Sum
from exceptiongroup import catch
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
# 使用 Django 的 Q 对象来构建复杂的查询条件
from django.db.models import Q


class Option(APIView):
    def get(self, request, tableName, columnName):
        try:
            print(tableName, columnName)
            level = request.query_params.get('level')
            parent = request.query_params.get('parent')
            ModelClass = apps.get_model(tableName, tableName.capitalize())
            # 基础查询，排除 null 和空字符串
            query = ModelClass.objects.filter(
                Q(**{f'{columnName}__isnull': False})
            )

            # 添加额外的查询条件，如果提供了 level 和 parent
            if level is not None:
                query = query.filter(level=level)
            if parent is not None:
                query = query.filter(parent=parent)

            # 获取 distinct 的 column_name 值
            # 注意：Django ORM 默认返回模型实例，要获取特定字段的 distinct 值，需要使用 values_list 和 distinct 方法
            options = query.values_list(columnName, flat=True).distinct()
            return Response({"code": 0, 'data': options})
        except Exception as e:
            return Response({"code": 500, "msg": '系统报错，请联系管理员'})


class Group(APIView):
    def get(self, request, tableName, columnName):
        ModelClass = apps.get_model(tableName, tableName.capitalize())
        query = ModelClass.objects.values(columnName).annotate(total=Count('*'))
        # 定义空列表
        result = []
        for item in query:
            # 定义空字典
            dict = {}
            dict[columnName] = item[columnName]
            dict['total'] = item['total']
            result.append(dict)
        return Response({"code": 0, 'data': result, 'msg': '统计成功'})


class Value(APIView):
    def get(self, request, tableName, xColumnName, yColumnName):
        ModelClass = apps.get_model(tableName, tableName.capitalize())
        query = ModelClass.objects.values(xColumnName).annotate(total=Sum(yColumnName))
        # 定义空列表
        result = []
        for item in query:
            # 定义空字典
            dict = {}
            dict[xColumnName] = item[xColumnName]
            dict['total'] = item['total']
            result.append(dict)
        return Response({"code": 0, 'data': result, 'msg': '统计成功'})