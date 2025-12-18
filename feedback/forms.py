from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        required=False,
        widget=forms.NumberInput(attrs={"type": "range", "min": "1", "max": "5"}),
    )

    class Meta:
        model = Feedback
        fields = ["name", "email", "phone", "subject", "category", "message", "rating"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ваше имя"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-input", "placeholder": "example@mail.ru"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "+7 (900) 123-45-67"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Тема обращения"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-textarea",
                    "placeholder": "Ваше сообщение...",
                    "rows": 5,
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "name": "Имя",
            "email": "Email",
            "phone": "Телефон",
            "subject": "Тема",
            "category": "Категория",
            "message": "Сообщение",
            "rating": "Оценка (1-5)",
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "")
        if phone and not any(char.isdigit() for char in phone):
            raise forms.ValidationError("Введите корректный номер телефона")
        return phone
