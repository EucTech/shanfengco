from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    context = {'title': 'Shan feng tyre repair company'}
    return render(request, 'layout.html', context)
