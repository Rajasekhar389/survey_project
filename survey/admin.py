from django.contrib.sites import admin

from .models import Question,Option,Response
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)