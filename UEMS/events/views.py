from django.shortcuts import render
from .models import Event

# Create your views here.
def events_home(request):
    events = Event.objects.all()
    return render(request, 'events/events_home.html',{'events': events})

def event_page(request, slug):
    event = Event.objects.get(slug=slug)
    return render(request, 'events/event_page.html', {'event':event})