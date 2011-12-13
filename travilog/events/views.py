from django.template import Context, loader
from events.models import Event
from django.http import HttpResponse

def index(request):
    latest_events = Event.objects.all().order_by('-date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'events': latest_events,
    })
    return HttpResponse(t.render(c))
	