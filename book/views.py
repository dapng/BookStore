from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForm, SaleBook
from . import models
from django.views.generic import DetailView, UpdateView, DeleteView


# def index(request):
#     return render(request, 'book/main.html')

def index(request):
    bk_list = Books.objects.order_by('-id')
    return render(request, 'book/main.html', {'bklist': bk_list})


def info(request):
    return render(request, 'book/info.html')


def book_home(request):
    books_list = Books.objects.order_by('-id')
    return render(request, 'book/book_list.html', {'books': books_list})


def book_info(request):
    books_list = Books.objects.order_by('-id')
    return render(request, 'book/sale_info.html', {'books': books_list})


def book_main(request):
    bk_list = Books.objects.order_by('-id')
    return render(request, 'book/main.html', {'bklist': bk_list})


class BooksDetailView(DetailView):
    model = Books
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BooksUpdateView(UpdateView):
    model = Books
    template_name = 'book/book_update.html'
    
    form_class = BooksForm


class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/home'
    template_name = 'book/book_delete.html'
    context_object_name = 'book'


def create(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верна'

    form = BooksForm()

    data = {
        'form': form,
        # 'error': error,
    }
    return render(request, 'book/book_create.html', data)


def sell_home(request):
    books_list = Books.objects.order_by('-id')
    return render(request, 'book/sell_home.html', {'books': books_list})


class BooksSaleDetailView(DetailView):
    model = Books
    template_name = 'book/sale_detail.html'
    context_object_name = 'sale-book'


class BooksSaleUpdateView(UpdateView):
    model = Books
    template_name = 'book/sale_update.html'
    context_object_name = 'sbook'

    form_class = SaleBook