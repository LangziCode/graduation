from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'orderid',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='订单编号'),
                    
                 ),
                            (
                    'tablename',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品表名'),
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
                            (
                    'goodid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='商品id'),
                    
                 ),
                            (
                    'goodname',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品名称'),
                    
                 ),
                            (
                    'picture',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品图片'),
                    
                 ),
                            (
                    'buynumber',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='购买数量'),
                    
                 ),
                            (
                    'price',
                    
                 ),
                            (
                    'discountprice',
                    
                 ),
                            (
                    'total',
                    
                 ),
                            (
                    'discounttotal',
                    
                 ),
                            (
                    'type',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='支付类型'),
                    
                 ),
                            (
                    'status',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='状态'),
                    
                 ),
                            (
                    'address',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='地址'),
                    
                 ),
            
            ],
            options={
                'db_table': 'orders',
            },
        ),



    ]
