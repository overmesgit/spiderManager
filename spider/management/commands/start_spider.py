from django.core.management import BaseCommand
from spider.spider import TitleSpider


class Command(BaseCommand):
    help = 'Start spider daemon'

    def handle(self, *args, **options):
        print 'Spider running, Ctrl-C for exit'
        try:
            spider = TitleSpider()
            spider.run()
        except KeyboardInterrupt:
            print 'Spider stopped'