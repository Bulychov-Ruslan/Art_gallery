from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Item, ItemAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')
    search_fields = ('id', 'content')


admin.site.register(Comment, CommentAdmin)

