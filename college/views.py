from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from college.models import College, Address, CollegeType
from event.models import Event

class CollegeListView(ListView):
    context_object_name = 'college_list'
    template_name = 'college/college_list.html'

    def get_queryset(self):
        return College.objects.all()


class CollegeDetailView(DetailView):
    context_object_name = 'college'
    model = College
    template_name='college/college_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailView, self).get_context_data(**kwargs)
        c = self.get_object()
        college_events = Event.objects.filter(college=c)
        context['college_events'] = college_events
        return context


class CollegeTypeListView(ListView):
    context_object_name = 'college_list'
    template_name='college/college_list.html'

    def get_queryset(self):
        slug_received = self.kwargs['slug']
        ct = get_object_or_404(CollegeType, slug=slug_received)
        return ct.college_set.all()
