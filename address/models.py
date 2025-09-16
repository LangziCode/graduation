from django.db import models

# Create your models here.

# 实体表
class Address(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    address = models.CharField(max_length=100, null=True, verbose_name='地址')
    name = models.CharField(max_length=100, null=True, verbose_name='收货人')
    phone = models.CharField(max_length=100, null=True, verbose_name='电话')
    isdefault = models.CharField(max_length=100, null=True, verbose_name='是否默认地址[是/否]')

    class Meta:
        db_table = 'address'

    def address_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'userid': instance.userid,
            'address': instance.address,
            'name': instance.name,
            'phone': instance.phone,
            'isdefault': instance.isdefault,
        }