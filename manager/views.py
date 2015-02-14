from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from manager.forms import ParserTaskForm
from manager.models import SiteUrl, ParserTask


class SiteUrlListView(CreateView):

    model = SiteUrl
    template_name = 'site_url_list_and_create.html'

    success_url = reverse_lazy('urls_list')

    def get_context_data(self, **kwargs):
        context = super(SiteUrlListView, self).get_context_data(**kwargs)
        context['urls_list'] = SiteUrl.objects.all()
        return context


class SiteUrlDeleteView(DeleteView):

    model = SiteUrl
    template_name = 'siteurl_confirm_delete.html'

    success_url = reverse_lazy('urls_list')


class ParserTaskListView(ListView):

    model = ParserTask
    template_name = 'parser_task_list.html'

    def get_queryset(self):
        return ParserTask.objects.order_by('-date')


class ParserTaskCreateView(CreateView):
    form_class = ParserTaskForm
    model = ParserTask
    success_url = reverse_lazy('parser_tasks_list')
    template_name = 'parser_task_create.html'


class ParserTaskDetailView(DetailView):
    model = ParserTask
    template_name = 'parser_task_detail.html'