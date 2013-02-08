from django.db import models
from django.contrib.auth.models import User

from college.models import College, Course
from event.models import Event, SubEvent

class Student(models.Model):
    user = models.ForeignKey(User)
    college = models.ForeignKey(College)
    course = models.ForeignKey(Course)
    batch = models.PositiveIntegerField(blank=True, null=True)
    event_attended = models.ManyToManyField(Event)
    event_participated = models.ManyToManyField(SubEvent)
