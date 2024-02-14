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
        fields = ['full_name', 'email', 'phone', 'company']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
        }

    # def clean_email(self):
    #     """This is to check if there is two emails"""
    #     email = self.cleaned_data['email']
    #     if Newsletter.objects.filter(email=email).exists():
    #         raise ValidationError("Email address already exists.")
    #     return email

