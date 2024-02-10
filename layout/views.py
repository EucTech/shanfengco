from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    context = {'title': 'Shan feng tire repair company'}
    return render(request, 'home.html', context)


def services(request):
    context = {'title': 'Services | Shan feng tire repair company'}
    return render(request, 'services.html', context)


def about(request):
    context = {'title': 'About | Shan feng tire repair company'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'title': 'contact | Shan feng tire repair company'}
    return render(request, 'contact.html', context)
