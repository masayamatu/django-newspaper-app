from django.contrib import admin

from .models import Article,Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article)
admin.site.register(Comment)
# Register your models here.
