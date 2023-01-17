from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader

from events.forms import EventForm, RegistrationForm
from events.models import Events, Registration


def home_page(request):
    return render(request, 'home_page.html')


@permission_required("events.add_events")
def create_event(request):
    if request.method == "POST":
        event_form = EventForm(request.POST, request.FILES)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Your event was successfully added!')
        else:
            messages.error(request, 'Error saving form')

        return redirect("events")
    event_form = EventForm()
    events = Events.objects.all()
    return render(request=request, template_name="create_event.html",
                  context={'event_form': event_form, 'events': events})


def delete_event(request, id):
    event = Events.objects.get(id=id)
    event.delete()
    return redirect('events')


def events(request):
    events = Events.objects.order_by('date')
    template = loader.get_template('all_events.html')
    context = {
        'events': events,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    try:
        event = Events.objects.get(id=id)
        viewed_post = request.session.get('viewed_post', [])
        if id not in viewed_post:
            viewed_post.append(id)
        request.session['viewed_post'] = viewed_post
        return render(request, 'details.html', {'event': event})
    except:
        return HttpResponseNotFound()


@login_required(login_url='/login')
def registration_to_event(request, id):
    event = Events.objects.get(id=id)
    if request.method == "POST":
        registration = Registration()
        registration.user = request.user
        registration.event = event
        registration.distance = request.POST['distance']
        if registration:
            registration.save()

            messages.success(request, 'You have successfully registered to event!')
        else:
            messages.error(request, 'Error saving form')

        return redirect("events")
    registrations = Registration.objects.all()
    return render(request=request, template_name="registration.html",
                  context={'registration_form': RegistrationForm, 'registrations': registrations, 'event': event, })

