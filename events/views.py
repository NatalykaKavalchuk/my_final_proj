from django.contrib import messages
from django.http import HttpResponse, FileResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader

from account.models import User
from events.forms import EventForm, SubmissionForm
from events.models import Events, Submission

from django.contrib.auth.decorators import permission_required, login_required


def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render({'title': 'Home page'}, request))


@permission_required("events.add_events")
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
    try:
        event = Events.objects.get(id=id)
        viewed_post = request.session.get('viewed_post', [])
        if id not in viewed_post:
            viewed_post.append(id)
        request.session['viewed_post'] = viewed_post
        return render(request, 'details.html', {'event': event})
    except:
        return HttpResponseNotFound()


def testing(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


@login_required(login_url='/login')
def registration_to_event(request, id):

    event = Events.objects.get(id=id)
    #
    # participant = User.objects.get(username=username)

    text_messages = ''

    if request.method == "POST":
        # event.participants.add(request.user)

        registration_form = SubmissionForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            text_messages = 'you have successfully registered!'
        else:
            text_messages = 'Error saving form'

        return redirect("events")
    registration_form = SubmissionForm()
    registrations = Submission.objects.all()
    return render(request=request, template_name="registration.html",
                  context={'registration_form': registration_form, 'registrations': registrations, 'event': event,
                           'text_messages': text_messages})
