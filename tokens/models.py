from django.db import models

# Create your models here.

# token表
class Token(models.Model):
    userid = models.IntegerField(max_length=100, null=True, blank=True, verbose_name='用户id')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='用户名')
    tablename = models.CharField(max_length=100, null=True, blank=True, verbose_name='表名')
    role = models.CharField(max_length=100, verbose_name='角色')
    token = models.CharField(max_length=100, verbose_name='token')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='新增时间')
    expiratedtime = models.DateTimeField(verbose_name='过期时间')

    class Meta:
        app_label = 'tokens'
        db_table = 'token'