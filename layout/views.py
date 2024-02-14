from django.shortcuts import render, redirect
from .forms import MessageForm, NewsletterForm
from .models import Newsletter
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
# from django.http import HttpResponse


def message_form(request):
    form = MessageForm()

    if request.method == 'POST':
        # if 'message-submit' in request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            company = form.cleaned_data['company']

            # context_variable = {
            #     'name': name,
            #     'email': email,
            #     'company': company,
            #     'message': message,
            # }

            # email_from = 'info@shanfengcoltd.com'
            # recipient = [email]

            # html_message = render_to_string('email.html', context_variable)

            # plain_message = strip_tags(html_message)

            # send_mail(
            #     subject='Receive email form form\'s message',
            #     message=plain_message,
            #     html_message=html_message,
            #     from_email=email_from,
            #     recipient_list=recipient
            # )

            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            # return redirect('home')
    return form


def news_letter(request):
    news_form = NewsletterForm()

    if 'newsletter-submit' in request.POST:
        news_form = NewsletterForm(request.POST)

        if news_form.is_valid():
            # messages.success(
            #     request, 'You have successfully subscribed to our newsletter!')
            # return redirect('home')
            email = news_form.cleaned_data['email']
            if Newsletter.objects.filter(email=email).exists():
                return JsonResponse({'error':'Email address already exists.'}, status=400)
            news_form.save()
        return email
    return news_form


def home(request):
    form = message_form(request)
    news_form = news_letter(request)
    context = {'title': 'Shan feng tire repair company'}
    return render(request, 'home.html', {'form': form, 'news_form': news_form, 'context': context})


def services(request):
    form = message_form(request)
    news_form = news_letter(request)
    context = {'title': 'Services | Shan feng tire repair company'}
    return render(request, 'services.html', {'form': form, 'news_form': news_form, 'context': context})


def about(request):
    form = message_form(request)
    news_form = news_letter(request)
    context = {'title': 'About | Shan feng tire repair company'}
    return render(request, 'about.html', {'form': form, 'news_form': news_form, 'context': context})


def contact(request):
    news_form = news_letter(request)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            return redirect('contact')
    context = {'title': 'contact | Shan feng tire repair company'}
    return render(request, 'contact.html', {'form': form, 'news_form': news_form, 'context': context})
