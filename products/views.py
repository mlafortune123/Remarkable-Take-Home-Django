from django.shortcuts import render
from django.db.models import Q
from .models import Book, Category, Tag

def book_list(request):
    print("Full GET data:", request.GET)
    books = Book.objects.select_related('category').prefetch_related('tags').all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    authors = Book.objects.values_list('author', flat=True).distinct().order_by('author')

    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')   
    tag_id = request.GET.get('tag', '')   
    selected_authors = request.GET.getlist('authors')

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if category_id:
        books = books.filter(category_id=category_id)

    if tag_id:
        books = books.filter(tags__id=tag_id)

    if selected_authors:
        books = books.filter(author__in=selected_authors)
    print("Selected authors:", selected_authors)
    print("All authors:", list(authors))
    books = books.distinct()
    context = {
        'books': books,
        'categories': categories,
        'tags': tags,
        'authors': authors,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tag': tag_id,
        'selected_authors': selected_authors
    }
    return render(request, 'products/book_list.html', context)