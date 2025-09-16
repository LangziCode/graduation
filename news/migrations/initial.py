from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'title',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='标题'),
                    
                 ),
                            (
                    'introduction',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='简介'),
                    
                 ),
                            (
                    'picture',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='图片'),
                    
                 ),
                            (
                    'content',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='内容'),
                    
                 ),
            
            ],
            options={
                'db_table': 'news',
            },
        ),



    ]
