from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from men.forms import AddArticleForm

from .models import *
menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},
        {'title': 'Sign in', 'url_name': 'login'},
        ]


class MenMain(ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Men.objects.filter(is_published=True)

# def index(request):
#
#     context = {
#         'menu': menu,
#         'title': 'Main page',
#         'cat_selected': 0,
#     }
#     return render(request, 'men/index.html', context=context)


def about(request):
    return render(request, 'men/about.html', {'menu': menu,
                                              'title': 'About site'})


class AddArticle(CreateView):
    form_class = AddArticleForm
    template_name = 'men/addarticle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add article'
        return context


# def addarticle(request):
#     if request.method == 'POST':
#         form = AddArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddArticleForm()
#     return render(request, 'men/addarticle.html', {'form': form, 'menu': menu,
#                                                    'title': 'Add article'})


def feedback(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sing in')


class ShowPost(DetailView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Men, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.full_name,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'men/post.html', context=context)


class MenCategory(ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category: ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Men.objects.filter(cat__url=self.kwargs['cat_slug'],
                                  is_published=True)


# def show_category(request, cat_id):
#
#     context = {
#         'menu': menu,
#         'title': 'Category List',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'men/index.html', context=context)
