from django import forms
from .models import CardSet, Card, Review

class CardSetForm(forms.ModelForm):
    class Meta:
        model = CardSet
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва набору'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис набору'}),
        }

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['term', 'definition']
        labels = {
            'term': 'Термін',         # Заміна "term" на "Термін"
            'definition': 'Опис',     # Заміна "definition" на "Опис"
        }
        widgets = {
            'term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть термін'}),
            'definition': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введіть опис'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Залиште коментар'}),
        }
