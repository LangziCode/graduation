from django.db import models

# Create your models here.

# 实体表
class Xuesheng(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    yonghuming = models.CharField(max_length=100, null=True, verbose_name='用户名')
    touxiang = models.CharField(max_length=100, null=True, verbose_name='头像')
    mima = models.CharField(max_length=100, null=True, verbose_name='密码')
    xingbie = models.CharField(max_length=100, null=True, verbose_name='性别')
    dianhua = models.CharField(max_length=100, null=True, verbose_name='电话')
    nicheng = models.CharField(max_length=100, null=True, verbose_name='昵称')
    rlimg = models.CharField(max_length=100, null=True, verbose_name='人脸图片')
    isws = models.IntegerField(null=True, verbose_name='是否完善')
    money = models.FloatField(null=True, verbose_name='余额')

    class Meta:
        db_table = 'xuesheng'

    def xuesheng_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'yonghuming': instance.yonghuming,
            'touxiang': instance.touxiang,
            'mima': instance.mima,
            'xingbie': instance.xingbie,
            'dianhua': instance.dianhua,
            'nicheng': instance.nicheng,
            'rlimg': instance.rlimg,
            'isws': instance.isws,
            'money': instance.money,
        }