from django.conf.urls.defaults import *
def local(name):
   return 'eksplane.interface.views.'+ name

urlpatterns = patterns('',
        (r'^$',      local('home'), None),
        (r'^(?P<object_id>\d+)/$', local('home'), None),
        (r'^ethtool/(?P<object_id>\d+)/$', local('ethtool'), None),
        (r'^ifconfig/(?P<object_id>\d+)/$', local('ifconfig'), None),
        (r'^ndd/(?P<object_id>\d+)/$', local('ndd'), None),
        (r'^netstat/(?P<object_id>\d+)/$', local('netstat'), None),
    )



