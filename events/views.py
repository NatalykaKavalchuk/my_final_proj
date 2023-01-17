from django.contrib import messages
from django.http import HttpResponse, FileResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader

from account.models import User
from events.forms import EventForm, RegistrationForm
from events.models import Events, Registration

from django.contrib.auth.decorators import permission_required, login_required


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


def testing(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())


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
            print("text")


            print("text")

            messages.success(request, 'You have successfully registered to event!')
        else:
            messages.error(request, 'Error saving form')

        return redirect("events")
    registrations = Registration.objects.all()
    return render(request=request, template_name="registration.html",
                  context={'registration_form': RegistrationForm, 'registrations': registrations, 'event': event, })






    #     # event.participants.add(request.user)
    #
    #     # registration_form = RegistrationForm(user=request.user, event=event, distance=request.POST['distance'])
    #     # registration_form = RegistrationForm()
    #     # registration_form.user = request.user
    #     # registration_form.event = event
    #     # registration_form.distance = request.POST['distance']
    #     # print(registration_form.is_valid())
    #     # registration_form.save()
    #     registration_form = Registration(request.POST, user=request.user, event=event)
    #     if registration_form:
    #
    #         registration_form.save()
    #         messages.success(request, 'You have successfully registered to event!')
    #     else:
    #         messages.error(request, 'Error saving form')
    #
    #     return redirect("events")
    # registrations = Registration.objects.all()
    # return render(request=request, template_name="registration.html",
    #               context={'registration_form': RegistrationForm, 'registrations': registrations, 'event': event, })
