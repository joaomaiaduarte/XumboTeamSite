from django.contrib import admin
from xt.models import Member, News, Image, Event

# Register your models here.
admin.site.register(Member)
admin.site.register(News)
admin.site.register(Image)
admin.site.register(Event)