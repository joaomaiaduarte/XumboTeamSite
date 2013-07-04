from django.shortcuts import render, render_to_response
from django.template import RequestContext
from xt.models import Member, News

def index(request):
    return render(request, 'xt/index.html')

def members(request):
    members = Member.objects.order_by('name')
    return render_to_response('xt/members.html', {'members' : members}, context_instance=RequestContext(request))

def recent_news(request):
    news = News.objects.order_by('-pub_date');
    return render_to_response('xt/recent_news.html', {'news' : news}, context_instance=RequestContext(request))

def track_list(request):
    return render(request, 'xt/track_list.html')

def next_events(request):
    return render(request, 'xt/next_events.html')

def past_events(request):
    return render(request, 'xt/past_events.html')