from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Book
from .forms import BookForm

# 1. Wyświetlanie Listy Książek i Filtrowanie
class BookListView(ListView):
    model = Book
    template_name = 'bookhome/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(author__icontains=query) | Q(title__icontains=query))

        return queryset

# 2. Dodawanie Książek
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookhome/book_form.html'
    success_url = reverse_lazy('book_list')

# 3. Edycja Książek
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookhome/book_form.html'
    success_url = reverse_lazy('book_list')

# 4. Usuwanie Książek
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'bookhome/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
