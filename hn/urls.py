from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
import news.api
import users.api

api = Api(api_name='v1')
api.register(news.api.ArticleResource())
api.register(users.api.UserRegistrationResource())
api.register(users.api.UserLoginResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^dashboard/', 'news.views.home', name='home'),
    url(r'^$', 'users.views.login', name='login'),
    url(r'^register/', 'users.views.register', name='register'),
    url(r'^logout/', 'users.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
