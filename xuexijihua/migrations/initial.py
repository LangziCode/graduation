from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xuexijihua',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'jihuamingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='计划名称'),
                    
                 ),
                            (
                    'tupian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='图片'),
                    
                 ),
                            (
                    'shangchuanshijian',
                                        models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
                    
                 ),
                            (
                    'jihuaxiangqing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='计划详情'),
                    
                 ),
                            (
                    'wanchengzhuangtai',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='完成状态'),
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
            
            ],
            options={
                'db_table': 'xuexijihua',
            },
        ),



    ]
