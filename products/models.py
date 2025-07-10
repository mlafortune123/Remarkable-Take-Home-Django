from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Book categories like Fiction, Non-Fiction, Science, etc."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, help_text="Brief description of this category")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        db_table = 'Categories'
    def __str__(self):
        return self.name

class Tag(models.Model):
    """Tags for books like 'bestseller', 'new-release', 'award-winner', etc."""
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#007bff', help_text="Hex color code for display")
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Main book model - renamed from Product to Book"""
    title = models.CharField(max_length=200, help_text="Book title")
    author = models.CharField(max_length=200, help_text="Author name(s)")
    description = models.TextField(help_text="Book description/summary")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price in dollars")
    pages = models.PositiveIntegerField(help_text="Number of pages")
    publication_date = models.DateField(help_text="When the book was published")
    
    # Relationships
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='books',
        help_text="Book category (Fiction, Science, etc.)"
    )
    tags = models.ManyToManyField(
        Tag, 
        blank=True, 
        related_name='books',
        help_text="Tags like 'bestseller', 'new-release', etc."
    )
    
    # Status fields
    stock_quantity = models.PositiveIntegerField(default=0, help_text="Number of copies in stock")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest books first
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
    
    @property
    def is_available(self):
        """Check if book is in stock and available"""
        return self.in_stock and self.stock_quantity > 0