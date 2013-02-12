from django.db import models
from django.contrib.auth.models import User

from college.models import College, Course
#from event.models import Event, SubEvent

class Student(models.Model):
    user = models.ForeignKey(User)
    college = models.ForeignKey(College)
    course = models.ForeignKey(Course)
    batch = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    event_attended = models.ManyToManyField('event.Event', null=True, blank=True)
    event_participated = models.ManyToManyField('event.SubEvent', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user.get_full_name())
