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
@time2:2019/10/31 10:12
@month2:十月
@email:datacraft@163.com
"""
from django import template

from blog.models import Post

register=template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    lastest_posts=Post.published.order_by('-publish')[:count]
    return {'latest_posts':lastest_posts}