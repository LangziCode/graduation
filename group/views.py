from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps

class Group(APIView):
    def get(self, request, tableName, columnName):
        ModelClass = apps.get_model(tableName, tableName.capitalize())
        query = ModelClass.objects.values(columnName).annotate(total=Count('*'))
        #定义空字典
        dict = {}
        # 定义空列表
        result = []
        for item in query:
            dict[columnName] = item[columnName]
            dict['total'] = item['total']
            result.append(dict)
        return Response({"code": 0, 'data': result, 'msg': '统计成功'})
