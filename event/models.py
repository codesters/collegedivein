from django.db import models
from django.contrib.auth.models import User

from college.models import College

class EventType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class SubEvent(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.name)


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
#    image = models.ImageField()

    def __unicode__(self):
        return unicode(self.name)


class Event(models.Model):

    name = models.CharField(max_length=300)
    event_type = models.ManyToManyField(EventType)
    description = models.TextField(null=True, blank=True)
    host = models.ForeignKey(College)
    college = models.CharField(max_length=300)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
#    image = models.ImageField()
    contacts = models.ManyToManyField(User)
    tcontacts = models.TextField(null=True, blank=True)
    sub_events = models.ManyToManyField(SubEvent)
    how_to_apply = models.TextField(null=True, blank=True)
    previous_events = models.ManyToManyField('self')
    website = models.URLField(null=True, blank=True)
    facebook_page = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    gallery = models.URLField(null=True, blank=True)
    event_registration = models.URLField(null=True, blank=True)
    rating = models.PositiveIntegerField(default=1)
    total_tickets = models.IntegerField(default=0)
    tickets_sold = models.IntegerField(default=0)
    last_date = models.DateField(blank=True, null=True)
    sponsors = models.ForeignKey(Sponsor)
#TODO change votes to PositiveSmallIntegerField
    votes = models.IntegerField(default=1)
    view = models.BooleanField(default=True)

    def _unicode__(self):
        return unicode(self.name)
