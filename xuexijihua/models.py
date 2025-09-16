from django.db import models

# Create your models here.

# 实体表
class Xuexijihua(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    jihuamingcheng = models.CharField(max_length=100, null=True, verbose_name='计划名称')
    tupian = models.CharField(max_length=100, null=True, verbose_name='图片')
    shangchuanshijian = models.DateField(auto_now_add=True, verbose_name='上传时间')
    jihuaxiangqing = models.CharField(max_length=100, null=True, verbose_name='计划详情')
    wanchengzhuangtai = models.CharField(max_length=100, null=True, verbose_name='完成状态')
    userid = models.IntegerField(null=True, verbose_name='用户id')

    class Meta:
        db_table = 'xuexijihua'

    def xuexijihua_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'jihuamingcheng': instance.jihuamingcheng,
            'tupian': instance.tupian,
            'shangchuanshijian': instance.shangchuanshijian,
            'jihuaxiangqing': instance.jihuaxiangqing,
            'wanchengzhuangtai': instance.wanchengzhuangtai,
            'userid': instance.userid,
        }