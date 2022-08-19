from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse_lazy
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(context_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'men/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title='Authentication')
        return dict(list(context.items()) + list(context_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
