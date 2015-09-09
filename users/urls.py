from django.conf.urls import patterns, include, url

from tastypie.api import Api

import users.api


urlpatterns = patterns('users.views',
    url(r'^login/$', 'user_login', name='user-login'),
    url(r'^logout/$', 'user_logout', name='user-logout'),
)

api = Api(api_name='v1')
api.register(users.api.UserLoginResource())

urlpatterns += patterns('',
    url(r'^api/', include(api.urls)),