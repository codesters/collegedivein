from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.dispatch import receiver
from allauth.account.signals import user_signed_up

from college.models import College, Course

class Student(models.Model):
    user = models.ForeignKey(User)
    college = models.ForeignKey(College)
    course = models.ForeignKey(Course)
    batch_start_year = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    events_attended = models.ManyToManyField('event.Event', null=True, blank=True)
    events_participated = models.ManyToManyField('event.SubEvent', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user.get_full_name())


@receiver(user_signed_up)
def group_assign(sender, user, request, **kwargs):
    student = Student.objects.get(user=user)
    g = Group.objects.get_or_create(name=student.college.slug)
    user.groups.add(g[0])
