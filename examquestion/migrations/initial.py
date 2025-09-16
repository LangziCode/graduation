from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examquestion',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'paperid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='所属测试卷id（外键）'),
                    
                 ),
                            (
                    'papername',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='测试卷名称'),
                    
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
                    'type',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）'),
                    
                 ),
                            (
                    'sequence',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='测试卷试题排序，值越大排越前面'),
                    
                 ),
            
            ],
            options={
                'db_table': 'examquestion',
            },
        ),



    ]
