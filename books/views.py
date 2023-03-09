from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import Resources, Category
from .forms import ResourcesForm
from django.http import HttpResponse


@login_required
def private_place(request):
    return HttpResponse("Shhh, members only!", content_type="text/plain")


@login_required
def list_books(request):
    books = Resources.objects.all()
    return render(request, 'books/index.html', {'books': books})


@user_passes_test(lambda user: user.is_staff)
def add_book(request):
    if request.method == 'POST':
        resources_form = ResourcesForm(request.POST, request.FILES)
        if resources_form.is_valid():
            resources_form.save()
            return redirect('home')
    form = ResourcesForm()
    return render(request, 'books/add_book.html', {'form': form})


@login_required
def detail_book(request, pk):
    book = get_object_or_404(Resources, pk=pk)
    return render(request, 'books/detail_book.html', {'book': book})


@user_passes_test(lambda user: user.is_staff)
def edit_book(request, pk):
    book = get_object_or_404(Resources, pk=pk)
    if request.method == 'POST':
        book_form = ResourcesForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('home')
    form = ResourcesForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'pk': pk})


@user_passes_test(lambda user: user.is_staff)
def delete_book(request, pk):
    book = get_object_or_404(Resources, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'books/delete_book.html')


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")


def resource_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    resources = Resources.objects.filter(category=category)
    return render(request, 'books/category.html', {'resources': resources})


def favorite_book(request, pk):
    resource = get_object_or_404(Resources, pk=pk)
    request.user.favorites.add(resource)
    return redirect('home')
