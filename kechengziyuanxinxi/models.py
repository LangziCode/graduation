from django.db import models

# Create your models here.

# 实体表
class Kechengziyuanxinxi(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    kechengmingcheng = models.CharField(max_length=100, null=True, verbose_name='课程名称')
    tupian = models.CharField(max_length=100, null=True, verbose_name='图片')
    kechengleixing = models.CharField(max_length=100, null=True, verbose_name='课程类型')
    kechengshipin = models.CharField(max_length=100, null=True, verbose_name='课程视频')
    fujian = models.CharField(max_length=100, null=True, verbose_name='附件')
    shangchuanshijian = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')
    beizhu = models.CharField(max_length=100, null=True, verbose_name='备注')
    xiangqing = models.CharField(max_length=100, null=True, verbose_name='详情')
    sfsh = models.CharField(max_length=100, null=True, verbose_name='是否审核')
    shhf = models.CharField(max_length=100, null=True, verbose_name='审核回复')

    class Meta:
        db_table = 'kechengziyuanxinxi'

    def kechengziyuanxinxi_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'kechengmingcheng': instance.kechengmingcheng,
            'tupian': instance.tupian,
            'kechengleixing': instance.kechengleixing,
            'kechengshipin': instance.kechengshipin,
            'fujian': instance.fujian,
            'shangchuanshijian': instance.shangchuanshijian,
            'beizhu': instance.beizhu,
            'xiangqing': instance.xiangqing,
            'sfsh': instance.sfsh,
            'shhf': instance.shhf,
        }