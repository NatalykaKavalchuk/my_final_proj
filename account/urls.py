from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

import account
import events.views
from account.views import ResetPasswordView, register_user

urlpatterns = [
    path('register', register_user, name='register'),
    path('login/', account.views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),

]