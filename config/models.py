from django.db import models

# Create your models here.


# 轮播图
class Config(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    value = models.CharField(max_length=100, verbose_name='图片参数')

    class Meta:
        db_table = 'config'