from django.shortcuts import render, redirect
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
