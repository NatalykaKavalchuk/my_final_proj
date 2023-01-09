from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
import events.views


urlpatterns = [
    path('', events.views.home_page, name='home_page'),
    path('create_event/', events.views.create_event, name='create_event'),
    path('events/', events.views.events, name='events'),
    path('events/details/<int:id>', events.views.details, name='details'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
