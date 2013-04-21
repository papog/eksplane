from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^(?P<object_path>.*)/$', 'eksplane.dirtree.views.show_path', None),
    )



