from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'author', 'post_data',
                    'post_category', 'post_published',)
    list_editable = ('post_published',)
    list_display_links = ('id', 'title',)
    summernote_fields = ('post_content',)


admin.site.register(Post, PostAdmin)
