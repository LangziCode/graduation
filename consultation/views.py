from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import myjwt
from .models import Consultation
from .serializers import ConsultationSer
from django.db.models import Q

@api_view(['GET'])
def query_msg(request):
    receiver = request.query_params.get('receiver')
    consultations = Consultation.objects.filter(Q(receiver=receiver) | Q(sender=receiver)).order_by('send_time')
    serializer = ConsultationSer(consultations, many=True)
    return Response({'code': 0,'data': serializer.data})

@api_view(['GET'])
def query_somebody_msg(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    self_id = myjwt.jwt_decode(token)['data']['userid']
    sender = request.query_params.get('sender')
    consultations = Consultation.objects.filter(
        (Q(receiver=self_id) & Q(sender=sender)) |
        (Q(receiver=sender) & Q(sender=self_id))
    ).order_by('send_time')
    serializer = ConsultationSer(consultations, many=True)
    return Response({'code': 0,'data': serializer.data})

@api_view(['POST'])
def update_read_status(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    self_id = myjwt.jwt_decode(token)['data']['userid']
    sender = request.data.get('sender')
    consultations = Consultation.objects.filter(sender=sender, receiver=self_id, read_status=0)
    consultations.update(read_status=1)
    return Response({'code': 0,'status': 'success'})