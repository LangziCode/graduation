from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examrecord',
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
                    'username',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名'),
                    
                 ),
                            (
                    'paperid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷id（外键）'),
                    
                 ),
                            (
                    'papername',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='测试卷名称'),
                    
                 ),
                            (
                    'questionid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷试题id（外键）'),
                    
                 ),
                            (
                    'questionname',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='测试卷试题名称'),
                    
                 ),
                            (
                    'options',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='选项，json字符串'),
                    
                 ),
                            (
                    'score',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='分值'),
                    
                 ),
                            (
                    'answer',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='正确答案'),
                    
                 ),
                            (
                    'analysis',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='答案解析'),
                    
                 ),
                            (
                    'myscore',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷试题得分'),
                    
                 ),
                            (
                    'myanswer',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='考生答案'),
                    
                 ),
            
            ],
            options={
                'db_table': 'examrecord',
            },
        ),



    ]
