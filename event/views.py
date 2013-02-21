import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from guardian.decorators import permission_required_or_403

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import UpdateView
from guardian.mixins import PermissionRequiredMixin

from django.shortcuts import get_object_or_404
from guardian.shortcuts import assign

from django.db.models.signals import post_save
from django.dispatch import receiver

from event.models import Event, EventType, Address, SubEvent
from student.models import Student

from event.forms import EventCreateForm, EventUpdateForm

@receiver(post_save, sender=Event)
def event_processing(sender, instance, created, **kwargs):
    s = instance.created_by.user
    assign('event.edit_event', s, instance)


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


class EventUserListView(ListView):
    context_object_name = 'events_created'
    template_name = 'event/event_user.html'

    def get_queryset(self):
        s = Student.objects.get(user=self.request.user)
        return Event.objects.filter(created_by=s).order_by('-created_on')


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

    def get_object(self):
        event = super(EventDetailView, self).get_object()
        event.view_count += 1
        event.save()
        return event


class EventTypeListView(ListView):
    context_object_name = 'event_list'
    template_name='event/event_list.html'

    def get_queryset(self):
        slug_received = self.kwargs['slug']
        et = get_object_or_404(EventType, slug=slug_received)
        return et.event_set.filter(start__gte=datetime.datetime.now())


class EventCreateView(CreateView):
    form_class = EventCreateForm
    template_name='event/event_create.html'

    def form_valid(self, form):
        s = Student.objects.get(user=self.request.user)
        form.instance.created_by = s
        form.instance.college = s.college #automaticllay instanciate college
        return super(EventCreateView, self).form_valid(form)

class EventUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = EventUpdateForm
    model = Event
    template_name = 'event/event_update.html'

    raise_exception = True
    permission_required = 'event.edit_event'
