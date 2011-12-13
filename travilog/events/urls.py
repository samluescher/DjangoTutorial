from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^hello/$', 'events.views.hello'),
    url(r'^$', 'events.views.index'),
)
