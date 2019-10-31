# -*- coding: utf-8 -*-
"""
       .__                         .__
______ |  |__   ____   ____   ____ |__|__  ___
\____ \|  |  \ /  _ \_/ __ \ /    \|  \  \/  /
|  |_> >   Y  (  <_> )  ___/|   |  \  |>    <
|   __/|___|  /\____/ \___  >___|  /__/__/\_ \
|__|        \/            \/     \/         \/
@project:pywork
@author:Phoenix
@file:mysite
@ide:PyCharm
@time2:2019/10/28 14:02
@month2:十月
@email:datacraft@163.com
"""
from django.urls import path
from blog.feeds import LatestPostsFeed
from blog import views

app_name='blog'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    # path('',views.PostListView.as_view(),name='post_list'),
    path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    path('<int:post_id>/share/',views.post_share,name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]