from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(MenMain.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addarticle/', AddArticle.as_view(), name='add_article'),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password/password_reset.html')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html')),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
             template_name='password/password_reset_confirm.html')),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'
    )),
    path('logout/', logout_user, name='logout'),
    path('signup/', RegisterUser.as_view(), name='sign_up'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MenCategory.as_view(), name='category'),
]
