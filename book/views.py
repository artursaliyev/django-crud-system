from django.shortcuts import render
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


class BookListView(ListView):
    model = Book


class BookCreateView(PassRequestMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_message = 'Success: Kitob qoshildi.'
    success_url = reverse_lazy('books:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/read_book.html'


class BookUpdateView(PassRequestMixin, SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_message = 'Success: Kitob yangilandi...'
    success_url = reverse_lazy('books:list')


class BookDeleteView(DeleteAjaxMixin, SuccessMessageMixin, DeleteView):
    model = Book
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('books:list')
    success_message = 'Delete: Book deleted...'




