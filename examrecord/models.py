from django.db import models

# Create your models here.

# 实体表
class Examrecord(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    username = models.CharField(max_length=100, null=True, verbose_name='用户名')
    paperid = models.IntegerField(null=True, verbose_name='测试卷id（外键）')
    papername = models.CharField(max_length=100, null=True, verbose_name='测试卷名称')
    questionid = models.IntegerField(null=True, verbose_name='测试卷试题id（外键）')
    questionname = models.CharField(max_length=100, null=True, verbose_name='测试卷试题名称')
    options = models.CharField(max_length=100, null=True, verbose_name='选项，json字符串')
    score = models.IntegerField(null=True, verbose_name='分值')
    answer = models.CharField(max_length=100, null=True, verbose_name='正确答案')
    analysis = models.CharField(max_length=100, null=True, verbose_name='答案解析')
    myscore = models.IntegerField(null=True, verbose_name='测试卷试题得分')
    myanswer = models.CharField(max_length=100, null=True, verbose_name='考生答案')

    class Meta:
        db_table = 'examrecord'

    def examrecord_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'userid': instance.userid,
            'username': instance.username,
            'paperid': instance.paperid,
            'papername': instance.papername,
            'questionid': instance.questionid,
            'questionname': instance.questionname,
            'options': instance.options,
            'score': instance.score,
            'answer': instance.answer,
            'analysis': instance.analysis,
            'myscore': instance.myscore,
            'myanswer': instance.myanswer,
        }