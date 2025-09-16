from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kechengziyuanxinxi',
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
                    'kechengleixing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='课程类型'),
                    
                 ),
                            (
                    'kechengshipin',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='课程视频'),
                    
                 ),
                            (
                    'fujian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='附件'),
                    
                 ),
                            (
                    'shangchuanshijian',
                    
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
                    'sfsh',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='是否审核'),
                    
                 ),
                            (
                    'shhf',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='审核回复'),
                    
                 ),
            
            ],
            options={
                'db_table': 'kechengziyuanxinxi',
            },
        ),



    ]
