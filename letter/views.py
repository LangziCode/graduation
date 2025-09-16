from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import myjwt
from .models import Letter
from .serializers import LetterSer
from django.db.models import Q

@api_view(['GET'])
def query_msg(request):
    receiver = request.query_params.get('receiver')
    letters = Letter.objects.filter(Q(receiver=receiver) | Q(sender=receiver)).order_by('send_time')
    serializer = LetterSer(letters, many=True)
    return Response({'code': 0, 'data': serializer.data})

@api_view(['GET'])
def query_somebody_msg(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    self_id = myjwt.jwt_decode(token)['data']['userid']
    sender = request.query_params.get('sender')
    letters = Letter.objects.filter(
        (Q(receiver=self_id) & Q(sender=sender)) |
        (Q(receiver=sender) & Q(sender=self_id))
    ).order_by('send_time')
    serializer = LetterSer(letters, many=True)
    return Response({'code': 0, 'data': serializer.data})

@api_view(['POST'])
def update_read_status(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    self_id = myjwt.jwt_decode(token)['data']['userid']
    sender = request.data.get('sender')
    letters = Letter.objects.filter(sender=sender, receiver=self_id, read_status=0)
    letters.update(read_status=1)
    return Response({'code': 0, 'status': 'success'})

@api_view(['GET'])
def query_letter_list(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    self_id = myjwt.jwt_decode(token)['data']['userid']
    # 查询与当前用户相关的私信列表
    letters = Letter.objects.filter(Q(receiver=self_id) | Q(sender=self_id)).distinct()
    serializer = LetterSer(letters, many=True)
    return Response({'code': 0, 'data': serializer.data})