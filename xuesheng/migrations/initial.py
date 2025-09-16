from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xuesheng',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'yonghuming',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名'),
                    
                 ),
                            (
                    'touxiang',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='头像'),
                    
                 ),
                            (
                    'mima',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='密码'),
                    
                 ),
                            (
                    'xingbie',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='性别'),
                    
                 ),
                            (
                    'dianhua',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='电话'),
                    
                 ),
                            (
                    'nicheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='昵称'),
                    
                 ),
                            (
                    'rlimg',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='人脸图片'),
                    
                 ),
                            (
                    'isws',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='是否完善'),
                    
                 ),
                            (
                    'money',
                    
                 ),
            
            ],
            options={
                'db_table': 'xuesheng',
            },
        ),



    ]
