from django.db import models

# Create your models here.

# 实体表
class News(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    title = models.CharField(max_length=100, null=True, verbose_name='标题')
    introduction = models.CharField(max_length=100, null=True, verbose_name='简介')
    picture = models.CharField(max_length=100, null=True, verbose_name='图片')
    content = models.CharField(max_length=100, null=True, verbose_name='内容')

    class Meta:
        db_table = 'news'

    def news_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'title': instance.title,
            'introduction': instance.introduction,
            'picture': instance.picture,
            'content': instance.content,
        }