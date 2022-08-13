from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView


from .forms import *
from .utils import *


class MenMain(DataMixin, ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(context_def.items()))

    def get_queryset(self):
        return Men.objects.filter(is_published=True)


def about(request):
    return render(request, 'men/about.html', {'menu': menu,
                                              'title': 'About site'})


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'men/addarticle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Add article')
        return dict(list(context.items()) + list(context_def.items()))


def feedback(request):
    return HttpResponse('Feedback')


def login(request):
    return HttpResponse('Sing in')


class ShowPost(DataMixin, DetailView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(context_def.items()))


class MenCategory(DataMixin, ListView):
    model = Men
    template_name = 'men/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Category: ' +
                                                  str(context['posts'][0].cat),
                                            cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(context_def.items()))

    def get_queryset(self):
        return Men.objects.filter(cat__url=self.kwargs['cat_slug'],
                                  is_published=True)
