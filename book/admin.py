from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'book_type', 'author', 'timestamp']
    list_display_links = ['title', 'book_type', 'author', 'timestamp']
    list_filter = ['title', 'book_type', 'author', 'timestamp']
    search_fields = ['title', 'book_type',]

    exclude = ['author']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Book, BookAdmin)


