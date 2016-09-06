from django.contrib import admin

from welcome.forms import BlogForm
from .models import Blog


class ArticleAdmin(admin.ModelAdmin):
    form = BlogForm


admin.site.register(Blog, ArticleAdmin)
