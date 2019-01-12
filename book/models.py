from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-id']


