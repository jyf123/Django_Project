"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from workapp import views # 在这里添加这一行代码，导入 views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('index.html', views.sub0),
    path('charts.html', views.sub1),
    path('panels.html', views.sub2),
    path('notifications.html', views.sub3),
    path('page-lockscreen.html', views.sub4),
    path('page-login.html', views.sub5),
    path('page-profile.html', views.sub6),
    path('typography.html', views.sub7),
    path('elements.html',views.sub8),
    path('tables.html',views.sub9),
    path('icons.html',views.sub10),
    path('page-charts.html',views.sub11),
    path('test.html',views.sub12),
    path('people.html',views.sub13)



    # path('upload1', views.upload1), # 人脸识别
    # path('upload2', views.upload2), # 场景分类
    # path('upload3', views.upload3), # 目标检测
    # path('upload4', views.upload4), # 视频异常检测
    # path('upload5', views.upload5), # 视频目标跟踪
    # path('upload6', views.upload6), # 语音识别

]
