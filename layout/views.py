from django.shortcuts import render, redirect
from .forms import MessageForm, NewsletterForm, RegisterForm, CustomAuthForm, SendNewsletter
from .models import Newsletter, Messages
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
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
            try:
                form = NewsletterForm(request.POST)
                if form.is_valid():
                    form.save()
                    full_name = form.cleaned_data['full_name']
                    sub_email = form.cleaned_data['email']
                    subject = 'Welcome to Shan Feng Co Tire Services Newsletter! 🚛' 
                    html_message = render_to_string(
                        'subscribe_email.html', {'full_name': full_name})
                    plain_message = strip_tags(html_message)
                    from_email = 'info@shanfengcoltd.com'
                    to = sub_email

                    mail = send_mail(subject, plain_message, from_email, [
                                     to], html_message=html_message)
                    if mail:
                        print("success ====>> ")
                        return JsonResponse({'message': 'Subscribed successfully!'}, status=200)
            except Exception as e:
                print("fail ====>> ")
                print(str(e))
    return HttpResponse(status=400)


def messages_form(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                full_name = form.cleaned_data['full_name']
                email = form.cleaned_data['email']
                company = form.cleaned_data['company']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']

                subject = 'Message from contact form'
                html_message = render_to_string(
                    'message_email.html', {'full_name': full_name,
                                            'company': company,
                                            'phone': phone,
                                            'email': email,
                                            'message': message})
                plain_message = strip_tags(html_message)
                from_email = email
                to = 'euccreative@gmail.com'

                mail = send_mail(subject, plain_message, from_email, [to], html_message=html_message)
                if mail:
                    print("success ====>> ")
                    return JsonResponse({'message': 'Your message has been sent successfully!'}, status=200)
            except Exception as e:
                print("fail ====>> ")
                print(str(e))
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
    title = 'Admin-login | Shan feng tire repair company'
    return render(request, 'admin_login.html', {'title': title, 'form': form})


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
@is_admin
def admin_dashboard(request):
    newsletter_emails = Newsletter.objects.values_list('email', flat=True)
    form = SendNewsletter()
    # form.fields['receivers'].initial = ','.join([active.email for active in Newsletter.objects.all()])
    form.fields['receivers'].initial = ','.join(newsletter_emails)

    if request.method == 'POST':
        form = SendNewsletter(request.POST)
        if form.is_valid():
            try:
                subject = form.cleaned_data.get('subject')
                receivers = form.cleaned_data.get('receivers').split(',')
                email_message = form.cleaned_data.get('message')

                print(email_message)

                html_content = render_to_string('send_newsletter.html', {
                                                'email_message': email_message})

                text_content = strip_tags(html_content)

                mail = EmailMultiAlternatives(
                    subject, text_content, bcc=receivers)
                mail.attach_alternative(html_content, "text/html")
                if mail.send():
                    print("success ====>> ")
                    messages.success(request, "Email sent successfully!")
            except Exception as e:
                print("fail ====>> ")
                print(str(e))
                messages.error(
                    request, f"There was an error sending email: {str(e)}")
        else:
            print("not valid ====>> ")
            for error in form.errors.values():
                messages.error(request, error)

        return redirect("admin_dashboard")

    form_messages = Messages.objects.order_by('-created_at').all()
    newsletters = Newsletter.objects.order_by('-join_at').all()

    # Paginate messages
    messages_paginator = Paginator(form_messages, 10)
    messages_page_number = request.GET.get('messages_page')
    messages_page_obj = messages_paginator.get_page(messages_page_number)

    # Paginate newsletters
    newsletters_paginator = Paginator(newsletters, 10)
    newsletters_page_number = request.GET.get('newsletters_page')
    newsletters_page_obj = newsletters_paginator.get_page(
        newsletters_page_number)

    is_messages_paginated = messages_paginator.num_pages > 0
    is_newsletters_paginated = newsletters_paginator.num_pages > 0

    title = 'Admin-dashboard | Shan feng tire repair company'
    return render(request, 'admin_dashboard.html', {
        'title': title,
        'form': form,
        'messages_page_obj': messages_page_obj,
        'newsletters_page_obj': newsletters_page_obj,
        'is_messages_paginated': is_messages_paginated,
        'is_newsletters_paginated': is_newsletters_paginated,
    })


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
