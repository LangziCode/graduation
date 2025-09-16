from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
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
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
                            (
                    'address',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='地址'),
                    
                 ),
                            (
                    'name',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='收货人'),
                    
                 ),
                            (
                    'phone',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='电话'),
                    
                 ),
                            (
                    'isdefault',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='是否默认地址[是/否]'),
                    
                 ),
            
            ],
            options={
                'db_table': 'address',
            },
        ),



    ]
