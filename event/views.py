import datetime
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
    template_name = 'event/event_list.html'

    def get_queryset(self):
        return Event.objects.filter(start__gte=datetime.datetime.now()).order_by('name')


class EventComingListView(ListView):
    context_object_name = 'event_list'
    template_name = 'event/event_list.html'

    def get_queryset(self):
        return Event.objects.filter(start__gte=datetime.datetime.now()).order_by('start')


class EventPopularListView(ListView):
    context_object_name = 'event_list'
    template_name = 'event/event_list.html'

    def get_queryset(self):
        return Event.objects.filter(start__gte=datetime.datetime.now()).order_by('-view_count')


class EventArchiveListView(ListView):
    context_object_name = 'event_list'
    template_name='event/event_list.html'

    def get_queryset(self):
        year = int(self.kwargs['year'])
        return Event.objects.filter(start__year=year).order_by('-start')


class EventDetailView(DetailView):
    context_object_name = 'event'
    model = Event
    template_name='event/event_detail.html'


class EventTypeListView(ListView):
    context_object_name = 'event_list'
    template_name='event/event_list.html'

    def get_queryset(self):
        event_type = get_object_or_404(EventType, id=self.kwargs['pk'])
        return Event.objects.filter(event_type=event_type).filter(start__gte=datetime.datetime.now())


class EventCreateView(CreateView):
    form_class = EventCreateForm
    template_name='event/event_create.html'

    def form_valid(self, form):
        s = Student.objects.get(user=self.request.user)
        form.instance.created_by = s
        if form.instance.college_is_venue:
            # Check if address already exixts
            if Address.objects.get(street__icontains = s.college.name):
                form.instance.venue = Address.objects.get(street__icontains=s.college.name)
            else:
                new_address = Address(street=s.college.name,\
                city=s.college.address.city,\
                state=s.college.address.state,\
                pincode=s.college.address.pincode,\
                country=s.college.address.country)
                new_address.save()
                form.instance.venue = new_address
        form.instance.college = s.college #automaticllay instanciate college
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(UpdateView):
    form_class = EventUpdateForm
    model = Event
    template_name = 'event/event_update.html'
