from django.conf.urls import patterns, url

from xt import views

urlpatterns = patterns('',
    url(r'^members$', views.members, name='members'),
    url(r'^recent_news$', views.recent_news, name='recent_news'),                
    url(r'^$', views.index, name='index'),
    url(r'^track_list$', views.track_list, name='track_list$'),
    url(r'^next_events', views.next_events, name='next_events'), 
    url(r'^past_events', views.past_events, name='past_events')  
)

