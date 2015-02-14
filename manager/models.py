from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class SiteUrl(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class SiteUrlParserResult(models.Model):
    result = models.TextField(blank=True)
    site_url = models.ForeignKey(SiteUrl)

    LOADING = 'lo'
    ERROR = 'er'
    COMPLETED = 'co'

    STATUS_CHOICES = (
        (LOADING, 'Loading'),
        (ERROR, 'Error'),
        (COMPLETED, 'Completed')
    )
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default=LOADING)


class ParserTask(models.Model):
    tasks = models.ManyToManyField(SiteUrl)
    results = models.ManyToManyField(SiteUrlParserResult, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def get_status(self):
        for result in self.results.all():
            if result.status == SiteUrlParserResult.ERROR:
                return SiteUrlParserResult.ERROR
            elif result.status == SiteUrlParserResult.COMPLETED:
                return SiteUrlParserResult.COMPLETED
        return SiteUrlParserResult.LOADING


def create_parsing_task_result(sender, **kwargs):
    if kwargs.get('action') == 'post_add':
        for site_url_id in kwargs['pk_set']:
            site_url_result = SiteUrlParserResult.objects.create(site_url_id=site_url_id)
            kwargs['instance'].results.add(site_url_result)

m2m_changed.connect(create_parsing_task_result, sender=ParserTask.tasks.through)