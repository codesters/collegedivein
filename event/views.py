from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404

from event.models import Event, EventType, Address, SubEvent
from student.models import Student

from event.forms import EventCreateForm, EventUpdateForm

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

class EventCreateView(CreateView):
    form_class = EventCreateForm
    template_name='event/event_create.html'

    def form_valid(self, form):
        s = Student.objects.get(user=self.request.user)
        form.instance.created_by = s
        return super(EventCreateView, self).form_valid(form)

class EventUpdateView(UpdateView):
    form_class = EventUpdateForm
    model = Event
    template_name = 'event/event_update.html'
