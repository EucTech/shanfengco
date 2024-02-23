from django.shortcuts import render, redirect
from .forms import MessageForm, NewsletterForm, RegisterForm, CustomAuthForm
from .models import Newsletter, Messages
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import is_admin
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


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

    title = 'Shan feng tire repair company'
    return render(request, 'home.html', {'form': form, 'news_form': news_form, 'title': title})


def services(request):
    form = MessageForm()
    news_form = NewsletterForm()
    title = 'Services | Shan feng tire repair company'
    return render(request, 'services.html', {'form': form, 'news_form': news_form, 'title': title})


def about(request):
    form = MessageForm()
    news_form = NewsletterForm()
    title = 'About | Shan feng tire repair company'
    return render(request, 'about.html', {'form': form, 'news_form': news_form, 'title': title})


def contact(request):
    news_form = NewsletterForm()
    form = MessageForm()
    title = 'contact | Shan feng tire repair company'
    return render(request, 'contact.html', {'form': form, 'news_form': news_form, 'title': title})


# def admin_signup(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             print("Registered =====>>>")
#             form.save()
#             return redirect('admin_login')
#     title = 'admin-signup | Shan feng tire repair company'
#     return render(request, 'admin_signup.html', {'title': title, 'form': form})


def admin_login(request):
    form = CustomAuthForm()

    if request.method == 'POST':
        form = CustomAuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], 
                                password=form.cleaned_data['password'])
            login(request, user)
            print('Authentication successful')
            next_page = request.GET.get('next', 'admin_dashboard')
            return redirect(next_page)
        else:
            print(form.errors)
            print('failed ===>>')
    title = 'admin-login | Shan feng tire repair company'
    return render(request, 'admin_login.html', {'title': title, 'form': form})


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
@is_admin
def admin_dashboard(request):

    messages = Messages.objects.order_by('created_at').all()
    newsletters = Newsletter.objects.order_by('join_at').all()

    
    # Paginate messages
    messages_paginator = Paginator(messages, 10)
    messages_page_number = request.GET.get('messages_page')
    messages_page_obj = messages_paginator.get_page(messages_page_number)

    # Paginate newsletters
    newsletters_paginator = Paginator(newsletters, 10)
    newsletters_page_number = request.GET.get('newsletters_page')
    newsletters_page_obj = newsletters_paginator.get_page(newsletters_page_number)


    title = 'admin-dashboard | Shan feng tire repair company'
    return render(request, 'admin_dashboard.html', {
        'title': title,
        'messages_page_obj': messages_page_obj,
        'newsletters_page_obj': newsletters_page_obj,
    })


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)

