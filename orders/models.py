from django.db import models

# Create your models here.

# 实体表
class Orders(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    orderid = models.CharField(max_length=100, null=True, verbose_name='订单编号')
    tablename = models.CharField(max_length=100, null=True, verbose_name='商品表名')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    goodid = models.IntegerField(null=True, verbose_name='商品id')
    goodname = models.CharField(max_length=100, null=True, verbose_name='商品名称')
    picture = models.CharField(max_length=100, null=True, verbose_name='商品图片')
    buynumber = models.IntegerField(null=True, verbose_name='购买数量')
    price = models.FloatField(null=True, verbose_name='价格/积分')
    discountprice = models.FloatField(null=True, verbose_name='折扣价格')
    total = models.FloatField(null=True, verbose_name='总价格/总积分')
    discounttotal = models.FloatField(null=True, verbose_name='折扣总价格')
    type = models.IntegerField(null=True, verbose_name='支付类型')
    status = models.CharField(max_length=100, null=True, verbose_name='状态')
    address = models.CharField(max_length=100, null=True, verbose_name='地址')

    class Meta:
        db_table = 'orders'

    def orders_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'orderid': instance.orderid,
            'tablename': instance.tablename,
            'userid': instance.userid,
            'goodid': instance.goodid,
            'goodname': instance.goodname,
            'picture': instance.picture,
            'buynumber': instance.buynumber,
            'price': instance.price,
            'discountprice': instance.discountprice,
            'total': instance.total,
            'discounttotal': instance.discounttotal,
            'type': instance.type,
            'status': instance.status,
            'address': instance.address,
        }