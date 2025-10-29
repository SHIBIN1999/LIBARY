from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('books/', views.books_view, name='books'),
    path('books/<pk>', views.books_view, name='books'), 
    path('unbook/', views.unbook_view, name='unbook'),
]
