from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name="Tytuł")
    author = models.CharField(max_length=150, verbose_name="Autor")
    publication_date = models.DateField(verbose_name="Data Wydania")

    class Meta:
        ordering = ['-publication_date'] 

    def get_absolute_url(self):
        return reverse('book_list')

    def __str__(self):
        return f"{self.title} ({self.author})"
