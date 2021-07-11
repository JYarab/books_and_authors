from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/create', views.create_book),
    path('books/<int:id>', views.book_info),
    path('books/add_author', views.add_author),
    path('authors', views.authors),
    path('authors/create', views.create_author),
    path('authors/<int:id>', views.author_info),
    path('authors/add_book', views.add_book),
]
