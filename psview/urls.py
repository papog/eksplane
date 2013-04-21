from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^$', 'eksplane.psview.views.list', None),
        (r'^(?P<object_id>\d+)/$', 'eksplane.psview.views.show_one_process', None),
    )



