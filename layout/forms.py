from django import forms
from .models import Messages, Newsletter
from django.core.exceptions import ValidationError


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['full_name', 'email', 'phone', 'company', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type message'}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['full_name', 'email', 'company']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
        }

