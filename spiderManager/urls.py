from django.conf.urls import patterns, include, url
from django.contrib import admin
from manager.views import SiteUrlListView, SiteUrlDeleteView, ParserTaskListView, ParserTaskCreateView, \
    ParserTaskDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', SiteUrlListView.as_view(), name='urls_list'),
    url(r'^siteUrls/delete/(?P<pk>\d+)/$', SiteUrlDeleteView.as_view(), name='delete_url'),
    url(r'^parserTasks/$', ParserTaskListView.as_view(), name='parser_tasks_list'),
    url(r'^parserTasks/create/$', ParserTaskCreateView.as_view(), name='parser_tasks_create'),
    url(r'^parserTasks/(?P<pk>\d+)/$', ParserTaskDetailView.as_view(), name='parser_tasks_detail'),
)
