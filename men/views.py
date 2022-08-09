from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.
from men.forms import AddArticleForm

from .models import *
menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Sign in', 'url_name': 'login'},
        ]


def index(request):

    context = {
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html', context=context)


def about(request):
    return render(request, 'men/about.html', {'menu': menu,
                                              'title': 'About site'})


def addarticle(request):
    if request.method == 'POST':
        form = AddArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddArticleForm()
    return render(request, 'men/addarticle.html', {'form': form, 'menu': menu,
                                                   'title': 'Add article'})


def feedback(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sing in')


def show_post(request, post_slug):
    post = get_object_or_404(Men, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.full_name,
        'cat_selected': post.cat_id,
    }

    return render(request, 'men/post.html', context=context)


def show_category(request, cat_id):

    context = {
        'menu': menu,
        'title': 'Category List',
        'cat_selected': cat_id,
    }
    return render(request, 'men/index.html', context=context)
