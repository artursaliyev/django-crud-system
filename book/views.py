from django.views.generic import (ListView, CreateView, DetailView, UpdateView, DeleteView)
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
import logging

logger = logging.getLogger('django')


class BookListView(ListView):
    model = Book
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(pk__gt=1).select_related('author').prefetch_related('tags')
        logger.info('book list')
        return qs


class BookCreateView(PassRequestMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('books:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        self.success_message = "{}: qoshildi".format(cleaned_data['title'])
        return self.success_message


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



