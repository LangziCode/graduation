from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jiaoshi',
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
                    'money',
                    
                 ),
            
            ],
            options={
                'db_table': 'jiaoshi',
            },
        ),



    ]
