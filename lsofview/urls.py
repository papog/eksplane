from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$', 'eksplane.lsofview.views.list', None),
        (r'^(?P<object_id>\d+)/$', 'eksplane.lsofview.views.show_one_process', None),
    )



