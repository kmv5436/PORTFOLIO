from django import forms
from .models import Contact
from .models import PatientReview


class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ваш телефон*'
        })
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ваше полное имя*'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ваш email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Опишите ваши симптомы и жалобы', 
                'rows': 4
            }),
        }
        labels = {
            'name': 'ФИО*',
            'email': 'Email',
            'phone': 'Телефон*',
            'message': 'Сообщение',
        }

from .models import PatientReview

class PatientReviewForm(forms.ModelForm):
    class Meta:
        model = PatientReview
        fields = ['name', 'email', 'phone', 'rating', 'review_text']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ваше имя*'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ваш email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ваш телефон'
            }),
            'rating': forms.RadioSelect(attrs={
                'class': 'rating-radio'
            }),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Поделитесь вашими впечатлениями от лечения...', 
                'rows': 5
            }),
        }
        labels = {
            'name': 'Ваше имя*',
            'email': 'Email',
            'phone': 'Телефон',
            'rating': 'Ваша оценка',
            'review_text': 'Текст отзыва*',
        }