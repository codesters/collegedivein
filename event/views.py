from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from event.models import Event, EventType, Address, SubEvent

class EventListView(ListView):
    context_object_name = 'event_list'
    model = Event
    template_name = 'event/event_list.html'


class EventDetailView(DetailView):
    context_object_name = 'event'
    model = Event
    template_name='event/event_detail.html'

class EventTypeListView(ListView):
    context_object_name = 'event_list'
    template_name='event/event_list.html'

    def get_queryset(self):
        event_type = get_object_or_404(EventType, id=self.kwargs['pk'])
        return Event.objects.filter(event_type=event_type)

