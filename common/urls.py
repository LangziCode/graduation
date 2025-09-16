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
    path('option/<str:tableName>/<str:columnName>', Option.as_view()),  # 下拉框
    path('group/<str:tableName>/<str:columnName>', Group.as_view()),  # 分组统计(单列分组统计数量)
    path('value/<str:tableName>/<str:xColumnName>/<str:yColumnName>', Value.as_view()) # 对x分组，统计y的总和
]