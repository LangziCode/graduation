from django.db import models

# Create your models here.


# 论坛
class Storeup(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    userid = models.IntegerField(verbose_name='用户id')
    refid = models.IntegerField(verbose_name='收藏id')
    tablename = models.CharField(max_length=200, verbose_name='表名')
    name = models.CharField(max_length=200, verbose_name='收藏名称')
    picture = models.CharField(max_length=200, verbose_name='收藏图片')
    type = models.CharField(max_length=200, verbose_name='类型(1:收藏,21:赞,22:踩)')

    class Meta:
        db_table = 'storeup'