from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *
menu = ['About site', 'Add article', 'Feedback', 'Sign in']

def index(request):
    posts = Men.objects.all()
    return render(request, 'men/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'men/about.html', {'menu': menu, 'title': 'About site'})


def categories(request, cat):
    return HttpResponse(f'<h1>News from categories</h1><p>{cat}</p>')

