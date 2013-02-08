from django.db import models

from college.models import College
from student.models import Student

class EventType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)


#class Sponsor(models.Model):
#    name = models.CharField(max_length=200)
#    description = models.TextField(null=True, blank=True)
#    website = models.URLField(blank=True, null=True)
#    image = models.ImageField()

#    def __unicode__(self):
#        return unicode(self.name)


PRIVACY_TYPE = ['Public', 'College', 'Private']


class Event(models.Model):
    name = models.CharField(max_length=120)
#    slug = models.SlugField()
    tagline = models.CharField(max_length=300)
    event_type = models.ManyToManyField(EventType)
    description = models.TextField(null=True, blank=True)
    host = models.ForeignKey(College)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
#    image = models.ImageField()
    coordinators = models.ManyToManyField(Student) #TODO event should remain their even if coordinators delete their accounts
    other_contacts = models.TextField(null=True, blank=True)
    privacy = models.CharField(max_length=30, choices = zip(PRIVACY_TYPE, PRIVACY_TYPE))
#    previous_events = models.ManyToManyField('self')
    social_website = models.URLField(null=True, blank=True)
    social_facebook = models.URLField(null=True, blank=True)
    social_twitter = models.URLField(null=True, blank=True)
    social_googleplus = models.URLField(null=True, blank=True)
    social_gallery = models.URLField(null=True, blank=True)
    social_email = models.EmailField(null=True, blank=True)
    votes = models.PositiveSmallIntegerField(default=1)
    show = models.BooleanField(default=True)

    def _unicode__(self):
        return unicode(self.name)


class SubEvent(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    event = models.ForeignKey(Event)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
#    image = models.ImageField()
    coordinators = models.ManyToManyField(Student, related_name='coordinators' ) #TODO only students of same college to be allowed
    winner1 = models.ForeignKey(Student, null=True, blank=True, related_name='winner1') 
    #TODO only participated students to be allowed - Try this in model form queryset or then with limit_choices_to
#    winner2 = models.ForeignKey(Student, null=True, blank=True, related_name='winner2')
#    winner3 = models.ForeignKey(Student, null=True, blank=True, related_name='winner3')
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.name)
