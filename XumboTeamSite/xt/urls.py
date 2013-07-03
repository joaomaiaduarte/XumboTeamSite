from django.conf.urls import patterns, url

from xt import views

urlpatterns = patterns('',
    url(r'^members$', views.members, name='members'),
    url(r'^recent_news$', views.recent_news, name='recent_news'),                
    url(r'^$', views.index, name='index')
)

