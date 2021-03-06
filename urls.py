from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eksplane/', include('eksplane.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),

     (r'^polls/', include('eksplane.polls.urls')),
     (r'^psview/', include('eksplane.psview.urls')),
     (r'^pstackview/', include('eksplane.pstackview.urls')),
     (r'^lsofview/', include('eksplane.lsofview.urls')),
    # new urls for object oriented interface
     (r'^computer/', include('eksplane.computer.urls')),
     (r'^dirtree/', include('eksplane.dirtree.urls')),
     (r'^file/', include('eksplane.file.urls')),
     (r'^module/', include('eksplane.module.urls')),
     (r'^interface/', include('eksplane.interface.urls')),
     (r'^package/', include('eksplane.package.urls')),
     (r'^port/', include('eksplane.port.urls')),
     (r'^process/', include('eksplane.process.urls')),
     (r'^window/', include('eksplane.window.urls')),


)
