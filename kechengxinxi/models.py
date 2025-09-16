from django.db import models

# Create your models here.

# 实体表
class Kechengxinxi(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    kechengmingcheng = models.CharField(max_length=100, null=True, verbose_name='课程名称')
    tupian = models.CharField(max_length=100, null=True, verbose_name='图片')
    shipin = models.CharField(max_length=100, null=True, verbose_name='视频')
    shangchuanshijian = models.DateField(auto_now_add=True, verbose_name='上传时间')
    beizhu = models.CharField(max_length=100, null=True, verbose_name='备注')
    xiangqing = models.CharField(max_length=100, null=True, verbose_name='详情')
    price = models.FloatField(null=True, verbose_name='价格')
    onelimittimes = models.IntegerField(null=True, verbose_name='单限')
    alllimittimes = models.IntegerField(null=True, verbose_name='库存')
    sfsh = models.CharField(max_length=100, null=True, verbose_name='是否审核')
    shhf = models.CharField(max_length=100, null=True, verbose_name='审核回复')

    class Meta:
        db_table = 'kechengxinxi'

    def kechengxinxi_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'kechengmingcheng': instance.kechengmingcheng,
            'tupian': instance.tupian,
            'shipin': instance.shipin,
            'shangchuanshijian': instance.shangchuanshijian,
            'beizhu': instance.beizhu,
            'xiangqing': instance.xiangqing,
            'price': instance.price,
            'onelimittimes': instance.onelimittimes,
            'alllimittimes': instance.alllimittimes,
            'sfsh': instance.sfsh,
            'shhf': instance.shhf,
        }