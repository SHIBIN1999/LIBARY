from django.shortcuts import render, redirect
from subapp.models import student



# ADD THIS NEW FUNCTION for books.html
def books_view(request):
    s = student.objects.all()  # Gets the SAME books as list view
    return render(request, 'books.html', {'s': s})

