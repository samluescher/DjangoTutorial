from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'events.views.index'),
    url(r'^add/$', 'events.views.add'),
    url(r'^(\d+)/edit/$', 'events.views.edit'),
)
