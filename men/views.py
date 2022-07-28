from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
menu = ['About site', 'Add article', 'Feedback', 'Sign in']

def index(request):
    return render(request, 'men/index.html', {'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'men/about.html', {'menu': menu, 'title': 'About site'})


def categories(request, cat):
    return HttpResponse(f'<h1>News from categories</h1><p>{cat}</p>')

