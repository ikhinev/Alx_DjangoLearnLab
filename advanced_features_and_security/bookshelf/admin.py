from django.contrib import admin
from .models import Book

# Register the Book model so it shows in the Django admin
admin.site.register(Book)
