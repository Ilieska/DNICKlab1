from django.contrib import admin
from .models import Book, Publisher

# Register your models here.

class BookAdmin (admin.ModelAdmin):
    
    list_display = ('title', 'isbn', 'publisher', 'publication_year', 'category', 'price')
    search_fields = ('title', 'isbn', 'publisher__name')
    list_filter = ('category', 'cover_type', 'publication_year')

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
          return True
        return False

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'founded_year', 'website')
    search_fields = ('name', 'country', 'city')

admin.site.register(Book, BookAdmin)