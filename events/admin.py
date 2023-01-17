from django.contrib import admin

from account.models import Profile
from events.models import Events, Registration


class EventsAdmin(admin.ModelAdmin):
    #
    # filter_horizontal = ['participants']

    list_display = ('id', 'title_event', 'registration_deadline', 'time_create', 'is_published')
    list_display_links = ('id', 'title_event')
    search_fields = ('title_event',)


admin.site.register(Events, EventsAdmin)


class RegistrationAdmin(admin.ModelAdmin):

    list_display = ('id', 'event',)
    list_display_links = ('id', 'event')
    search_fields = ('event',)


admin.site.register(Registration, RegistrationAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('email',)


admin.site.register(Profile, ProfileAdmin)
