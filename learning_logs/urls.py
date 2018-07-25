#coding=gbk
"""����learning_logs��URLģʽ"""
from django.urls import path,re_path
from . import views
app_name='learning_logs'
urlpatterns = [
    # ��ҳ
    path('',views.index,name='index'),
    # ��ʾ���е�����
    re_path(r'^topics/$',views.topics,name='topics'),
    # �ض��������ϸҳ��
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    # ����������������ҳ
    re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
    # �����������Ŀ��ҳ��
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    # ���ڱ༭��Ŀ��ҳ��
    re_path(r'^edit_entry/(?P<entry_id>\d+)$',views.edit_entry,name='edit_entry')
]
