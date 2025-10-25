from django.urls import path,include
from . import views
urlpatterns = [

path('books/', views.books_view, name='books'),  # Display page
# path('list/', views.list_view, name='list'),      # Admin page
]