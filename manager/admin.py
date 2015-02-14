from django.contrib import admin

# Register your models here.
from manager.models import ParserTask, SiteUrlParserResult

admin.site.register(ParserTask)
admin.site.register(SiteUrlParserResult)