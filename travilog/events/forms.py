from events.models import Event
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model = Event
