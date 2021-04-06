from django.contrib import admin
from .models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_name', 'comment_email',
                    'comment_post', 'comment_data', 'comment_published', )
    list_editable = ('comment_published', )
    list_display_links = ('id', 'comment_name', 'comment_email', )


admin.site.register(Comments, CommentAdmin)
