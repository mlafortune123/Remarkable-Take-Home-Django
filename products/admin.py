from django.contrib import admin
from .models import Book, Category, Tag
# Register your models here.
# products/admin.py

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'book_count']
    search_fields = ['name']
    list_editable = ['color']
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'price', 'stock_quantity', 'created_at']
    list_filter = ['category', 'tags', 'publication_date', 'created_at']
    search_fields = ['title', 'author', 'description']
    filter_horizontal = ['tags']  # Nice interface for many-to-many
    list_editable = ['price', 'stock_quantity']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'publication_date'  # Date drill-down
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'description')
        }),
        ('Publishing Details', {
            'fields': ('publication_date', 'pages', 'price')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Inventory', {
            'fields': ('stock_quantity',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse')  # Collapsible section
        }),
    )