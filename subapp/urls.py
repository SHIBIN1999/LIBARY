
from django.urls import path
from .views import list,create,view,delete,edit

urlpatterns = [
    path('',create,name='create'),
    path('view/',view,name='view'),
    path('list/',list,name='list'),
    path('edit/<pk>',edit,name='edit'),
    path('delete/<pk>',delete,name='delete')
]