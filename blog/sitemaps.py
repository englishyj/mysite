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
@time2:2019/10/31 14:12
@month2:十月
@email:datacraft@163.com
"""
from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq='weekly'
    priority=0.9

    def items(self):
        return Post.published.all()

    def lastmod(self,obj):
        return obj.updated