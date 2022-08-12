from django.urls import path

from .views import *

urlpatterns = [
    path('', MenMain.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MenCategory.as_view(), name='category'),
]
