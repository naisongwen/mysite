from django.contrib import admin

# Register your models here.

from .models import Question,Article

admin.site.register(Question)
admin.site.register(Article)
