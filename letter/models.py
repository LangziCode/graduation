from django.db import models

# Create your models here.


# 私信
class Letter(models.Model):
    sender = models.IntegerField(verbose_name='发送者Id')
    sender_name = models.CharField(max_length=200, verbose_name='发送者昵称')
    receiver = models.IntegerField(verbose_name='接受者id')
    receiver_name = models.CharField(max_length=200, verbose_name='接收者昵称')
    msg = models.CharField(max_length=200, verbose_name='消息内容')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    read_status = models.IntegerField(verbose_name='是否已读')

    class Meta:
        db_table = 'letter'