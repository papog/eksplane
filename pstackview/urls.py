from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^(?P<object_id>\d+)/$', 'eksplane.pstackview.views.show_one_process', None),
    )



