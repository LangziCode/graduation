from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messagess',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='留言人id'),
                    
                 ),
                            (
                    'username',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名'),
                    
                 ),
                            (
                    'content',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='留言内容'),
                    
                 ),
                            (
                    'cpicture',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='留言图片'),
                    
                 ),
                            (
                    'reply',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='回复内容'),
                    
                 ),
                            (
                    'rpicture',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='回复图片'),
                    
                 ),
            
            ],
            options={
                'db_table': 'messagess',
            },
        ),



    ]
