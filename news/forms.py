from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date', 'name']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Основной текст'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор (Никнейм, ФИО)'
            }),
        }

