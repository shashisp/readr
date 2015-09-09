from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
import news.api

api = Api(api_name='v1')
api.register(news.api.ArticleResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
