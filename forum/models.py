from django.db import models

# Create your models here.


# 论坛
class Forum(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    title = models.CharField(max_length=200, verbose_name='帖子标题')
    content = models.CharField(max_length=1000, verbose_name='帖子内容')
    parentid = models.IntegerField(verbose_name='父节点id')
    userid = models.IntegerField(verbose_name='用户id')
    username = models.CharField(max_length=200, verbose_name='用户名')
    isdone = models.CharField(max_length=200, verbose_name='状态')

    class Meta:
        db_table = 'forum'