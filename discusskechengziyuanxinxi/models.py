from django.db import models

# Create your models here.

# 实体表
class Discusskechengziyuanxinxi(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    refid = models.IntegerField(null=True, verbose_name='关联表id')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    nickname = models.CharField(max_length=100, null=True, verbose_name='用户名')
    content = models.CharField(max_length=100, null=True, verbose_name='评论内容')
    reply = models.CharField(max_length=100, null=True, verbose_name='回复内容')

    class Meta:
        db_table = 'discusskechengziyuanxinxi'

    def discusskechengziyuanxinxi_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'refid': instance.refid,
            'userid': instance.userid,
            'nickname': instance.nickname,
            'content': instance.content,
            'reply': instance.reply,
        }