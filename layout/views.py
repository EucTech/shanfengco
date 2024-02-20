from django.shortcuts import render, redirect
from .forms import MessageForm, NewsletterForm
from .models import Newsletter
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.http import HttpResponse


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if Newsletter.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email is already subscribed.'}, status=400)
        else:
            form = NewsletterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Subscribed successfully!'}, status=200)
    return HttpResponse(status=400)


def messages_form(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Your message has been sent successfully!'}, status=200)
    return HttpResponse(status=400)


def home(request):
    news_form = NewsletterForm()
    form = MessageForm()

    context = {'title': 'Shan feng tire repair company'}
    return render(request, 'home.html', {'form': form, 'news_form': news_form, 'context': context})


def services(request):
    form = MessageForm()
    news_form = NewsletterForm()
    context = {'title': 'Services | Shan feng tire repair company'}
    return render(request, 'services.html', {'form': form, 'news_form': news_form, 'context': context})


def about(request):
    form = MessageForm()
    news_form = NewsletterForm()
    context = {'title': 'About | Shan feng tire repair company'}
    return render(request, 'about.html', {'form': form, 'news_form': news_form, 'context': context})


def contact(request):
    news_form = NewsletterForm()
    form = MessageForm()
    context = {'title': 'contact | Shan feng tire repair company'}
    return render(request, 'contact.html', {'form': form, 'news_form': news_form, 'context': context})
