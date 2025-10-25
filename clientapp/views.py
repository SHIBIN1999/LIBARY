from django.shortcuts import redirect, render
from . models import Book

def books_view(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'s': books})