from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(Commemts)
admin.site.register(CommentFile)