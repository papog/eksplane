from django.conf.urls.defaults import *
def local(name):
   return 'eksplane.package.views.'+ name

urlpatterns = patterns('',
        (r'^$',      local('home'), None),
         (r'^(?P<object_id>\d+)/$', local('home'), None),
         (r'^dependencies/(?P<object_id>\d+)/$', local('dependencies'), None),
         (r'^info/(?P<object_id>\d+)/$', local('info'), None),
         (r'^list/(?P<object_id>\d+)/$', local('list'), None),
    )



