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
    path('page', CartPage.as_view()),  # 分页查询
    path('list', CartList.as_view()),  # 分页查询
    path('save', CartSave.as_view()), # 保存
    path('add', CartSave.as_view()), # 保存
    path('update', CartUpdate.as_view()),  # 更新信息
    path('delete', CartDelete.as_view()), # 删除信息
    path('info/<int:id>', CartInfo.as_view()),  # 查询详情数据
    path('detail/<int:id>', CartInfo.as_view()),  # 帖子详情

]