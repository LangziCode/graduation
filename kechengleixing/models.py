from django.db import models

# Create your models here.

# 实体表
class Kechengleixing(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    kechengleixing = models.CharField(max_length=100, null=True, verbose_name='课程类型')
    shangchuanshijian = models.DateField(auto_now_add=True, verbose_name='上传时间')

    class Meta:
        db_table = 'kechengleixing'

    def kechengleixing_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'kechengleixing': instance.kechengleixing,
            'shangchuanshijian': instance.shangchuanshijian,
        }