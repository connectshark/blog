from django.contrib import admin

# Register your models here.
from article.models import Article, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content']
    list_display_links = ['article']
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']
    class Meta:
        model = Comment

admin.site.register(Article)
admin.site.register(Comment, CommentModelAdmin)