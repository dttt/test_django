from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5
    url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/result
    url(r'^(?P<poll_id>\d+)/result/$', views.ResultView.as_view(), name='result'),
    # ex: /polls/5/vote
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)