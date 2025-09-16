from django.db import models

# Create your models here.

# 实体表
class Examquestion(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    paperid = models.IntegerField(null=True, verbose_name='所属测试卷id（外键）')
    papername = models.CharField(max_length=100, null=True, verbose_name='测试卷名称')
    questionname = models.CharField(max_length=100, null=True, verbose_name='测试卷试题名称')
    options = models.CharField(max_length=100, null=True, verbose_name='选项，json字符串')
    score = models.IntegerField(null=True, verbose_name='分值')
    answer = models.CharField(max_length=100, null=True, verbose_name='正确答案')
    analysis = models.CharField(max_length=100, null=True, verbose_name='答案解析')
    type = models.IntegerField(null=True, verbose_name='测试卷试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）')
    sequence = models.IntegerField(null=True, verbose_name='测试卷试题排序，值越大排越前面')

    class Meta:
        db_table = 'examquestion'

    def examquestion_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'paperid': instance.paperid,
            'papername': instance.papername,
            'questionname': instance.questionname,
            'options': instance.options,
            'score': instance.score,
            'answer': instance.answer,
            'analysis': instance.analysis,
            'type': instance.type,
            'sequence': instance.sequence,
        }