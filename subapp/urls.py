
from django.urls import path
from .views import list,create,view,delete,edit,bookeduser

urlpatterns = [
    path('create/',create,name='create'),
    path('view/',view,name='view'),
    path('',list,name='list'),
    path('edit/<pk>',edit,name='edit'),
    path('delete/<pk>',delete,name='delete'),
    path('bookeduser/',bookeduser,name='bookeduser'),
]