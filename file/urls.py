from django.conf.urls.defaults import *
def local(name):
   return 'eksplane.file.views.'+ name

urlpatterns = patterns('',
        (r'^$',      local('home'), None),
        (r'^(?P<object_id>\d+)/$', local('home'), None),
        (r'^associated/(?P<object_id>\d+)/$', local('associated'), None),
        (r'^baobab/(?P<object_id>\d+)/$', local('baobab'), None),
        (r'^contents/(?P<object_id>\d+)/$', local('contents'), None),
        (r'^fuser/(?P<object_id>\d+)/$', local('fuser'), None),
        (r'^head/(?P<object_id>\d+)/$', local('head'), None),
        (r'^hexedit/(?P<object_id>\d+)/$', local('hexedit'), None),
        (r'^nm/(?P<object_id>\d+)/$', local('nm'), None),
        (r'^tail/(?P<object_id>\d+)/$', local('tail'), None),
        (r'^treeview/(?P<object_id>\d+)/$', local('treeview'), None),
        
    )



