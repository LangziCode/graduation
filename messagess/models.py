from django.db import models

# Create your models here.

# 实体表
class Messagess(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    userid = models.IntegerField(null=True, verbose_name='留言人id')
    username = models.CharField(max_length=100, null=True, verbose_name='用户名')
    content = models.CharField(max_length=100, null=True, verbose_name='留言内容')
    cpicture = models.CharField(max_length=100, null=True, verbose_name='留言图片')
    reply = models.CharField(max_length=100, null=True, verbose_name='回复内容')
    rpicture = models.CharField(max_length=100, null=True, verbose_name='回复图片')

    class Meta:
        db_table = 'messagess'

    def messagess_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'userid': instance.userid,
            'username': instance.username,
            'content': instance.content,
            'cpicture': instance.cpicture,
            'reply': instance.reply,
            'rpicture': instance.rpicture,
        }