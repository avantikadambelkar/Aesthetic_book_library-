from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'reading_status', 'rating', 'user', 'is_featured', 'created_at')
    list_filter = ('genre', 'reading_status', 'rating', 'is_featured', 'created_at')
    search_fields = ('title', 'author', 'description', 'aesthetic_tag', 'isbn')
    list_editable = ('reading_status', 'rating', 'is_featured')
