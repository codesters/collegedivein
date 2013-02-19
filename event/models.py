import datetime
from django.db import models
from django.core.urlresolvers import reverse

from college.models import College, Address
from student.models import Student

STATES = (
    'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh', 'Assam', 'Meghalaya', 'Manipur',\
    'Mizoram','Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal', 'Rajasthan', 'Gujarat', 'Maharashtra', 'Goa',\
    'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh')

PRIVACY_TYPE = ['Public', 'College', 'Private']

class EventType(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('event_type', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.name)


class Event(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    tagline = models.CharField(max_length=300, null=True, blank=True)
    event_type = models.ForeignKey(EventType)
    has_sub_events = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    college = models.ForeignKey(College)
    college_is_venue = models.BooleanField(default=True)
    venue = models.ForeignKey(Address, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    last_date_for_registration = models.DateField(null=True, blank=True)
    host_on_cdi = models.BooleanField(default=True)
    created_by = models.ForeignKey(Student, blank=True, null=True, on_delete=models.SET_NULL, related_name='event_creator')
    created_on = models.DateField(auto_now_add=True)
    coordinators = models.ManyToManyField(Student, blank=True, null=True) #TODO event should remain their even if coordinators delete their accounts
    other_contacts = models.TextField(null=True, blank=True)
    privacy = models.CharField(max_length=30, choices = zip(PRIVACY_TYPE, PRIVACY_TYPE))
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    googleplus = models.URLField(null=True, blank=True)
    gallery = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    view_count = models.BigIntegerField(default=1)
    show = models.BooleanField(default=True)

    class Meta:
        permissions = (
                ('Can view Event', 'view_event'),
                ('Can edit Event', 'edit_event'),
                )

    def save(self, *args, **kwargs):
        if self.college_is_venue:
            self.venue = self.college.address
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return unicode(self.name)


class SubEvent(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    event = models.ForeignKey(Event)
    start = models.DateTimeField()
    end = models.DateTimeField()
    local_venue = models.CharField(max_length=300, blank=True, null=True)
    coordinators = models.ManyToManyField(Student, null=True, blank=True, related_name='coordinators' ) #TODO only students of same college to be allowed
    winner = models.ForeignKey(Student, null=True, blank=True, related_name='winner')
    #TODO only participated students to be allowed - Try this in model form queryset or then with limit_choices_to
    show = models.BooleanField(default=True)

#    def get_absolute_url(self):
#        return reverse('sub_event_detail', kwargs={'slug': self.slug})

    class Meta:
        permissions = (
                ('view_subevent', 'view_subevent'),
                ('edit_subevent', 'edit_subevent'),
                )

    def __unicode__(self):
        return unicode(self.name)
