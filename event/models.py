from django.db import models
from django.core.urlresolvers import reverse

from college.models import College
from student.models import Student

STATES = (
    'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh', 'Assam', 'Meghalaya', 'Manipur',\
    'Mizoram','Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal', 'Rajasthan', 'Gujarat', 'Maharashtra', 'Goa',\
    'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh')

PRIVACY_TYPE = ['Public', 'College', 'Private']

class EventType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('event_types', args=str(self.id))

    def __unicode__(self):
        return unicode(self.name)


class Address(models.Model):
    street = models.CharField(max_length=300, blank=True, default='')
    city = models.CharField(max_length=100, default='New Delhi')
    state = models.CharField(max_length=40, choices = zip(STATES, sorted(STATES)))
    pincode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=120, default='India')

    def __unicode__(self):
        return unicode('%s %s' %(self.street, self.city))


class Event(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField() #TODO add automatics completion with name in admin.py
    tagline = models.CharField(max_length=300)
    event_type = models.ManyToManyField(EventType)
    description = models.TextField(null=True, blank=True)
    college = models.ForeignKey(College)
    college_is_venue = models.BooleanField(default=True)
    venue = models.ForeignKey(Address, null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    last_date_for_registration = models.DateField(null=True, blank=True)
    thmubnail = models.URLField()
    created_by = models.ForeignKey(Student, blank=True, null=True, on_delete=SET_NULL, related_name='event_creater')
    coordinators = models.ManyToManyField(Student) #TODO event should remain their even if coordinators delete their accounts
    other_contacts = models.TextField(null=True, blank=True)
    privacy = models.CharField(max_length=30, choices = zip(PRIVACY_TYPE, PRIVACY_TYPE))
    website = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    googleplus = models.URLField(null=True, blank=True)
    gallery = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    votes = models.PositiveSmallIntegerField(default=1)
    show = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('event_detail', args=str(self.id)) #TODO connect absolute url of event with slug

    def __unicode__(self):
        return unicode(self.name)


class SubEvent(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    event = models.ForeignKey(Event)
    start = models.DateTimeField()
    end = models.DateTimeField()
    thumbnail = models.URLField(null=True, blank=True)
    local_venue = models.CharField(max_length=300, blank=True, null=True)
    coordinators = models.ManyToManyField(Student, related_name='coordinators' ) #TODO only students of same college to be allowed
    winner1 = models.ForeignKey(Student, null=True, blank=True, related_name='winner1') 
    #TODO only participated students to be allowed - Try this in model form queryset or then with limit_choices_to
#    winner2 = models.ForeignKey(Student, null=True, blank=True, related_name='winner2')
#    winner3 = models.ForeignKey(Student, null=True, blank=True, related_name='winner3')
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.name)
