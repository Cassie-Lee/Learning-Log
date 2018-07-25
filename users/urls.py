#coding=gbk
"""ΪӦ�ó���users����URLģʽ"""
from django.urls import re_path
from django.contrib.auth.views import login

from . import views

app_name='users'
urlpatterns=[
    # ��¼ҳ��
    re_path(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    # ע��
    re_path(r'^logout/$',views.logout_view,name='logout'),
    # ע��ҳ��
    re_path(r'^register/$',views.register,name='register'),
]
