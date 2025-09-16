"""springboot4oKm0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('save', Save.as_view()),  # 添加帖子
    path('add', Save.as_view()),  # 添加帖子
    path('page', Page.as_view()),  # 获取帖子
    path('flist', List.as_view()),  # 获取帖子
    path('delete', ForumDelete.as_view()),  # 删除帖子
    path('update', ForumUpdate.as_view()),  # 修改帖子
    path('info/<int:id>', Info.as_view()),  # 帖子详情
    path('list/<int:id>', ListInfo.as_view()),  # 修改帖子
    path('detail/<int:id>', Info.as_view()),  # 帖子详情
]