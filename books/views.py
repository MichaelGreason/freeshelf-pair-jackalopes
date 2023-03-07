from django.shortcuts import render, redirect, get_object_or_404
from .models import Resources
from .forms import ResourcesForm


def list_books(request):
    books = Resources.objects.all()
    return render(request, 'books/index.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        resources_form = ResourcesForm(request.POST)
        if resources_form.is_valid():
            resources_form.save()
            return redirect('home')
    form = ResourcesForm()
    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, pk):
    book = get_object_or_404(Resources, pk=pk)
    if request.method == 'POST':
        book_form = ResourcesForm(request.POST, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('home')
    form = ResourcesForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'pk': pk})
