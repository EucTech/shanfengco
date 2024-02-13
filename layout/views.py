from django.shortcuts import render, redirect
from .forms import MessageForm, NewsletterForm
from django.contrib import messages
from django import forms
from django.core.exceptions import ValidationError
# from django.http import HttpResponse


def home(request):
    form = MessageForm()
    news_form = NewsletterForm()

    if request.method == 'POST':
        if 'message-submit' in request.POST:
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('home')
        
        elif 'newsletter-submit' in request.POST:
            news_form = NewsletterForm(request.POST)
            
            if news_form.is_valid():   
                news_form.save()
                messages.success(request, 'You have successfully subscribed to the newsletter!')
                return redirect('home')

    context = {'title': 'Shan feng tire repair company'}
    return render(request, 'home.html', {'form': form, 'news_form': news_form, 'context': context})

def services(request):
    context = {'title': 'Services | Shan feng tire repair company'}
    return render(request, 'services.html', context)


def about(request):
    context = {'title': 'About | Shan feng tire repair company'}
    return render(request, 'about.html', context)


def contact(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    context = {'title': 'contact | Shan feng tire repair company'}
    return render(request, 'contact.html', {'form': form, 'context': context})
