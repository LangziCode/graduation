from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kechengleixing',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'kechengleixing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='课程类型'),
                    
                 ),
                            (
                    'shangchuanshijian',
                                        models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
                    
                 ),
            
            ],
            options={
                'db_table': 'kechengleixing',
            },
        ),



    ]
