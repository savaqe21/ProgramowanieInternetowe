from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data Wydania'
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']