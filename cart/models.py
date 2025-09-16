from django.db import models

# Create your models here.

# 实体表
class Cart(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    tablename = models.CharField(max_length=100, null=True, verbose_name='商品表名')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    goodid = models.IntegerField(null=True, verbose_name='商品id')
    goodname = models.CharField(max_length=100, null=True, verbose_name='商品名称')
    picture = models.CharField(max_length=100, null=True, verbose_name='图片')
    buynumber = models.IntegerField(null=True, verbose_name='购买数量')
    price = models.FloatField(null=True, verbose_name='单价')
    discountprice = models.FloatField(null=True, verbose_name='会员价')

    class Meta:
        db_table = 'cart'

    def cart_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'tablename': instance.tablename,
            'userid': instance.userid,
            'goodid': instance.goodid,
            'goodname': instance.goodname,
            'picture': instance.picture,
            'buynumber': instance.buynumber,
            'price': instance.price,
            'discountprice': instance.discountprice,
        }