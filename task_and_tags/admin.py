from django.contrib import admin

from task_and_tags.models import Tasks, Tag

admin.site.register(Tasks)
admin.site.register(Tag)
