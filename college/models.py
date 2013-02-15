from django.db import models
from django.core.urlresolvers import reverse


STATES = (
    'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh', 'Assam', 'Meghalaya', 'Manipur',\
    'Mizoram','Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal', 'Rajasthan', 'Gujarat', 'Maharashtra', 'Goa',\
    'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh')


class Course(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    duration = models.SmallIntegerField(default=3)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return unicode(self.name)


class Address(models.Model):
    street = models.CharField(max_length=350, blank=True, default = '')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=40, choices=zip(sorted(STATES), sorted(STATES)))
    pincode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=120, default='India')

    def meta(self):
        verbose_name_plural = 'addresses'

    def __unicode__(self):
        return unicode('%s %s' %(self.street, self.city))


class CollegeType(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('college_type', kwargs={'slug':self.slug})

    def __unicode__(self):
        return unicode(self.name)

class College(models.Model):
    name=models.CharField(max_length=300)
    slug = models.SlugField()
    college_type=models.ForeignKey(CollegeType)
    about = models.TextField(default = '')
    address = models.ForeignKey(Address)
    estd = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    courses = models.ManyToManyField(Course)
    rating = models.PositiveIntegerField(default=1)

    def get_absolute_url(self):
        return reverse('college_detail', kwargs={'slug':self.slug})

    def __unicode__(self):
        return unicode(self.name)

