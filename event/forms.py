from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from event.models import Event

from django.contrib.admin import widgets

class EventCreateForm(ModelForm):
    start = forms.DateTimeField(widget = widgets.AdminSplitDateTime)
    end = forms.DateTimeField(widget = widgets.AdminSplitDateTime)
    class Meta:
        model=Event
        exclude = ('created_by', 'show', 'votes', 'coordinators',)


class EventUpdateForm(ModelForm):
    start = forms.DateTimeField(widget = widgets.AdminSplitDateTime)
    end = forms.DateTimeField(widget = widgets.AdminSplitDateTime)
    class Meta:
        model=Event
        exclude = ('created_by', 'show', 'votes', 'coordinators',)
