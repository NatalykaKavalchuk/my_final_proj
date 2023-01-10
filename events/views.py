from django.contrib import messages
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render, redirect
from django.template import loader

from events.forms import EventForm
from events.models import Events


def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render({'title': 'Home page'}))


def create_event(request):
    if request.method == "POST":
        event_form = EventForm(request.POST, request.FILES)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, ('Your event was successfully added!'))
        else:
            messages.error(request, 'Error saving form')

        return redirect("events")
    event_form = EventForm()
    events = Events.objects.all()
    return render(request=request, template_name="create_event.html",
                  context={'event_form': event_form, 'events': events})


def events(request):
    events = Events.objects.order_by('date')
    template = loader.get_template('all_events.html')
    context = {
        'events': events,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    event = Events.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'event': event,
    }
    return HttpResponse(template.render(context, request))



