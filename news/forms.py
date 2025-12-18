from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.utils import timezone
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
                'type': 'datetime-local',  # HTML5 datetime picker
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор (Никнейм, ФИО)'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Устанавливаем текущую дату по умолчанию
        if not self.instance.pk:  # Только для новых статей
            from django.utils import timezone
            self.initial['date'] = timezone.now()