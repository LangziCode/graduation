from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exampaper',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'name',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='测试卷名称'),
                    
                 ),
                            (
                    'time',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='等级测试时长(分钟)'),
                    
                 ),
                            (
                    'status',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷状态'),
                    
                 ),
            
            ],
            options={
                'db_table': 'exampaper',
            },
        ),



    ]
