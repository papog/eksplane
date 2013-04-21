from django.conf.urls.defaults import *
def local(name):
   return 'eksplane.computer.views.'+ name

urlpatterns = patterns('',
        (r'^$',      local('home'), None),
        (r'cpuinfo/$', local('cpuinfo'), None),
        (r'dmesg/$', local('dmesg'), None),
        (r'lshal/$', local('lshal'), None),
        (r'lsmod/$', local('smod'), None),
        (r'lspackages/$', local('lspackages'), None),
        (r'lspci/$', local('lspci'), None),
        (r'lsusb/$', local('lsusb'), None),
        (r'free/$', local('free'), None),
    )



