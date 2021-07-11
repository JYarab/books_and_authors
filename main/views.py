from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request, 'books.html', context)

def create_book(request):
    Book.objects.create(
        title=request.POST['title'], 
        description=request.POST['desc'])
    return redirect('/')

def book_info(request, id):
    context = {
        "book" : Book.objects.get(id=id),
        "authors" : Author.objects.all()
    }
    return render(request, 'book_info.html', context)

def add_author(request):
    this_book = request.POST['book']
    this_author = request.POST['author']
    Book.objects.get(id=this_book).authors.add(Author.objects.get(id=this_author))
    return redirect(f'/books/{this_book}')

def authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        notes=request.POST['notes'])
    return redirect('/authors')

def author_info(request, id):
    context = {
        "books" : Book.objects.all(),
        "author" : Author.objects.get(id=id)
    }
    return render(request, 'author_info.html', context)

def add_book(request):
    this_book = request.POST['book']
    this_author = request.POST['author']
    Author.objects.get(id=this_author).books.add(Book.objects.get(id=this_book))
    return redirect(f'/authors/{this_author}')
