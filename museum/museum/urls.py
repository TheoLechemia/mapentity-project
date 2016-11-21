from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
'',
#url(r'^$', 'main.views.home', name='home'),
url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout',),
url(r'', include('mapentity.urls', namespace='mapentity', app_name='mapentity')),
url(r'^paperclip/', include('paperclip.urls')),
url(r'', include('main.urls', namespace='main', app_name='main')),
url(r'^admin/', include(admin.site.urls)),
)
