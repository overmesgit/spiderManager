import os
from time import sleep
from grab.spider import Spider, Task
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderManager.settings'
django.setup()
from manager.models import SiteUrlParserResult


class TitleSpider(Spider):
    def task_generator(self):
        while True:
            next_task = SiteUrlParserResult.objects.filter(status=SiteUrlParserResult.LOADING).first()
            if next_task:
                yield Task('download', url=next_task.site_url.url, instance=next_task, priority=1)
            else:
                sleep(1)

    def task_download(self, grab, task):
        title = grab.pyquery('title').text()
        task.instance.result = title
        task.instance.status = SiteUrlParserResult.COMPLETED
        task.instance.save()

    def task_download_fallback(self, task):
        task.instance.result = 'Connection error'
        task.instance.status = SiteUrlParserResult.ERROR
        task.instance.save()