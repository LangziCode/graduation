from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discusskechengxinxi',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'refid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='关联表id'),
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
                            (
                    'nickname',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名'),
                    
                 ),
                            (
                    'content',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='评论内容'),
                    
                 ),
                            (
                    'reply',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='回复内容'),
                    
                 ),
            
            ],
            options={
                'db_table': 'discusskechengxinxi',
            },
        ),



    ]
