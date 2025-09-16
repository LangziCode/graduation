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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('py003/address/', include('address.urls')),
        path('py003/orders/', include('orders.urls')),
        path('py003/cart/', include('cart.urls')),
        path('py003/news/', include('news.urls')),
        path('py003/messagess/', include('messagess.urls')),
        path('py003/exampaper/', include('exampaper.urls')),
        path('py003/examquestion/', include('examquestion.urls')),
        path('py003/examrecord/', include('examrecord.urls')),
        path('py003/kechengxinxi/', include('kechengxinxi.urls')),
        path('py003/discusskechengxinxi/', include('discusskechengxinxi.urls')),
        path('py003/kechengziyuanxinxi/', include('kechengziyuanxinxi.urls')),
        path('py003/discusskechengziyuanxinxi/', include('discusskechengziyuanxinxi.urls')),
        path('py003/kechengleixing/', include('kechengleixing.urls')),
        path('py003/xuexijihua/', include('xuexijihua.urls')),
        path('py003/jiaoshi/', include('jiaoshi.urls')),
        path('py003/xuesheng/', include('xuesheng.urls')),

    path('py003/users/', include('users.urls')),
    path('py003/forum/', include('forum.urls')),
    path('py003/storeup/', include('storeup.urls')),
    path('py003/config/', include('config.urls')),
    path('py003/file/', include('file.urls')),
    path('py003/', include('common.urls')),
    path('py003/consultation/', include('consultation.urls')),
    path('py003/letter/', include('letter.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)