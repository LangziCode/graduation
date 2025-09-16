from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kechengxinxi',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'kechengmingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='课程名称'),
                    
                 ),
                            (
                    'tupian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='图片'),
                    
                 ),
                            (
                    'shipin',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='视频'),
                    
                 ),
                            (
                    'shangchuanshijian',
                                        models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
                    
                 ),
                            (
                    'beizhu',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
                    
                 ),
                            (
                    'xiangqing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='详情'),
                    
                 ),
                            (
                    'price',
                    
                 ),
                            (
                    'onelimittimes',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='单限'),
                    
                 ),
                            (
                    'alllimittimes',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='库存'),
                    
                 ),
                            (
                    'sfsh',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='是否审核'),
                    
                 ),
                            (
                    'shhf',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='审核回复'),
                    
                 ),
            
            ],
            options={
                'db_table': 'kechengxinxi',
            },
        ),



    ]
