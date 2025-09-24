from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get("q")
    if query:
        # ✅ safe ORM query (avoids SQL injection)
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})
