from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data wydarzenia'
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'date']

class CommentForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['event', 'author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Napisz swój komentarz...'}),
            'author': forms.TextInput(attrs={'placeholder': 'Twoja nazwa (opcjonalnie)'}),
        }