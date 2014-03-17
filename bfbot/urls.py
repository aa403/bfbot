from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from bfbot_core.views import *
from bfbot import settings

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'bfbot.views.home', name='home'),
	url(r'^bfbot/', include('bfbot_core.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', serverLinks.root, name='rootpage'),

	# login / logout pages
	url(r'^login/$', serverLinks.login, name='login_page'),
	url(r'^create_user/$', serverLinks.create_user, name='create_user'),
	url(r'^do_login/$', serverLinks.do_login, name='do_login'),
	url(r'^do_logout/$', serverLinks.do_logout, name='do_logout'),

)

urlpatterns += patterns('',
						(
						r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)