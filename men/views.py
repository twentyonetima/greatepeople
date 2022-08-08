from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *
menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Sign in', 'url_name': 'login'},
        ]


def index(request):
    posts = Men.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html', context=context)


def about(request):
    return render(request, 'men/about.html', {'menu': menu, 'title': 'About site'})


def addarticle(request):
    return HttpResponse('Add article')


def feedback(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sing in')


def show_post(request, post_id):
    return HttpResponse(f'Show article with id = {post_id}')


def show_category(request, cat_id):
    posts = Men.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Category List',
        'cat_selected': cat_id,
    }
    return render(request, 'men/index.html', context=context)
