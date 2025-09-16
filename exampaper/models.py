from django.db import models

# Create your models here.

# 实体表
class Exampaper(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    name = models.CharField(max_length=100, null=True, verbose_name='测试卷名称')
    time = models.IntegerField(null=True, verbose_name='等级测试时长(分钟)')
    status = models.IntegerField(null=True, verbose_name='测试卷状态')

    class Meta:
        db_table = 'exampaper'

    def exampaper_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'name': instance.name,
            'time': instance.time,
            'status': instance.status,
        }