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
@time2:2019/10/31 14:39
@month2:十月
@email:datacraft@163.com
"""
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from blog.models import Post


class LatestPostsFeed(Feed):
    title='博客'
    link='/blog/'
    description_template = '我的新日志'

    def item(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body,30)