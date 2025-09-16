from django.db import models

# Create your models here.


# 管理员表
class Users(models.Model):
    username = models.CharField(max_length=100, null=True, verbose_name='管理员用户名')
    password = models.CharField(max_length=100, null=True, verbose_name='管理员密码')
    role = models.CharField(max_length=100, null=True, verbose_name='角色', default='管理员')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'users'