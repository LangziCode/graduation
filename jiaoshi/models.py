from django.db import models

# Create your models here.

# 实体表
class Jiaoshi(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    yonghuming = models.CharField(max_length=100, null=True, verbose_name='用户名')
    mima = models.CharField(max_length=100, null=True, verbose_name='密码')
    xingbie = models.CharField(max_length=100, null=True, verbose_name='性别')
    dianhua = models.CharField(max_length=100, null=True, verbose_name='电话')
    nicheng = models.CharField(max_length=100, null=True, verbose_name='昵称')
    money = models.FloatField(null=True, verbose_name='余额')

    class Meta:
        db_table = 'jiaoshi'

    def jiaoshi_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'yonghuming': instance.yonghuming,
            'mima': instance.mima,
            'xingbie': instance.xingbie,
            'dianhua': instance.dianhua,
            'nicheng': instance.nicheng,
            'money': instance.money,
        }