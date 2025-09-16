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
    path('save', Save.as_view()),  # 添加轮播图
    path('page', Page.as_view()),  # 获取轮播图列表
    path('list', List.as_view()),  # 获取轮播图列表
    path('info/<int:id>', Info.as_view()),  # 获取单个轮播图详细信息
    path('update', Update.as_view()),  # 修改轮播图
    path('delete', Delete.as_view()),  # 删除轮播图 （前端暂时没有按键）
]