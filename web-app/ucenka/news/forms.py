from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименования'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "date": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата публикации'

            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва'
            })
        }
