from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

from account.forms import LoginForm
# from account.forms import LoginForm
from account.views import CustomLoginView, ResetPasswordView, register_user
from django.contrib.auth import views as auth_views

import events.views


urlpatterns = [
    path('', events.views.home_page, name='home_page'),
    path('create_event/', events.views.create_event, name='create_event'),
    path('events/', events.views.events, name='events'),
    path('events/details/<int:id>', events.views.details, name='details'),
    path('events/registration', events.views.registration_to_event, name='registration'),
    path('test/', events.views.testing, name='test'),
    path('account/register.html', register_user, name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(template_name='registration/password_reset.html'), name='password_reset'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
