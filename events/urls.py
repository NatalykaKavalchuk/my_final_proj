from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

import account
import events.views
from account.views import ResetPasswordView, register_user

urlpatterns = [
    path('', events.views.home_page, name='home_page'),
    path('create_event/', events.views.create_event, name='create_event'),
    path('events/', events.views.events, name='events'),
    path('events/details/<int:id>', events.views.details, name='details'),
    path('events/delete_event/<int:id>', events.views.delete_event, name='delete-event'),
    path('events/details/<int:id>/registration', events.views.registration_to_event, name='registration'),
    path('account/register.html', register_user, name='register'),
    path('login/', account.views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
