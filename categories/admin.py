from django.contrib import admin
from .models import Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat')
    list_display_links = ('id', 'name_cat')


admin.site.register(Categories, CategoriesAdmin)
