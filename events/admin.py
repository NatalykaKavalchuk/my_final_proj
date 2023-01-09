from django.contrib import admin
from events.models import Events


class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_event', 'time_create', 'is_published')
    list_display_links = ('id', 'title_event')
    search_fields = ('title_event',)


admin.site.register(Events, EventsAdmin)
