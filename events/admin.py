from django.contrib import admin

from events.models import Events, Submission


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_event', 'registration_deadline', 'time_create', 'is_published')
    list_display_links = ('id', 'title_event')
    search_fields = ('title_event',)


admin.site.register(Events, EventsAdmin)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'participant')
    list_display_links = ('id', 'event')
    search_fields = ('event',)


admin.site.register(Submission, SubmissionAdmin)
