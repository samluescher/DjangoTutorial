from events.models import Event
from events.forms import EventForm
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response


def index(request):
    latest_events = Event.objects.all().order_by('-date')
    c = RequestContext(request, {
        'events': latest_events,
    })
    t = loader.get_template('events/index.html')
    return HttpResponse(t.render(c))


def add(request):

    if request.method == "GET":
        form = EventForm()
    elif request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events.views.index'))

    c = RequestContext(request)
    c.update({
        'form': form,
    })

    t = loader.get_template('events/add.html')
    return HttpResponse(t.render(c))


def edit(request, object_id):
    try:
        event = Event.objects.get(pk=object_id)
    except Event.DoesNotExist:
        raise Http404()

    if request.method == "GET":
        form = EventForm(instance=event)
    elif request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('events.views.index'))    

    c = RequestContext(request)
    c.update({
        'form': form,
    })

    return render_to_response('events/add.html', context_instance=c)    
    # shortcut replaces::
    #   t = loader.get_template('events/add.html')
    #   return HttpResponse(t.render(c))
