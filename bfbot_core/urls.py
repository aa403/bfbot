from django.conf.urls import patterns, url
from bfbot_core.views import *



urlpatterns = patterns('',

    # url(r'testvis/$', temp.demo_linechart, name='testvis'),
    url(r'^$', serverLinks.root1, name='rootpage1'),
    url(r'main/$', main.firstpage, name='main'),
    url(r'test/$', main.testConnection, name='main'),


)

