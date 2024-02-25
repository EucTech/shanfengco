from django import forms
from .models import Messages, Newsletter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from tinymce.widgets import TinyMCE


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


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    is_admin = forms.BooleanField(label="Is Admin", required=False)

    class Meta:
        model = User
        fields = ['username', 'is_admin', 'password1', 'password2']


class CustomAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Please enter a correct username and password.'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class PlainTextTinyMCE(TinyMCE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['tinymce'] = {
            'selector': 'textarea',
            'plugins': 'textcolor',
            'toolbar': 'undo redo | formatselect | bold italic | forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat',
            'menubar': False,
            'valid_elements': ''
        }


class SendNewsletter(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=PlainTextTinyMCE(), label="Email content")
