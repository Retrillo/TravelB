from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Article

class ArticleForm(ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
        }),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            'anons': TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Основной текст'}),
        }
