from django.db import models


COLLEGE_TYPE = ('Arts/Commerce/Science', 'Engineering', 'Management', 'Law', 'Medical/Dental', 'University', 'Other')

STATES = (
    'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh', 'Assam', 'Meghalaya', 'Manipur',\
    'Mizoram','Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal', 'Rajasthan', 'Gujarat', 'Maharashtra', 'Goa',\
    'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh')


class Course(models.Model):

    name = models.CharField(max_length=60)
    full_name = models.CharField(max_length = 300)
    duration = models.SmallIntegerField(default=3)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Address(models.Model):
    street = models.CharField(max_length=350, blank=True, default = '')
    city = models.CharField(max_length=100, default='New Delhi')
    state = models.CharField(max_length=40, choices=zip(STATES, sorted(STATES)))
    pincode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=120, default='India')

    def __unicode__(self):
        return '%s %s' %(self.street, self.city)



class College(models.Model):

    name=models.CharField(max_length=300)
    full_name = models.CharField(max_length=300)
    college_type=models.CharField(max_length = 40, choices =zip(COLLEGE_TYPE, COLLEGE_TYPE))
    about = models.TextField(default = '')
    address = models.ForeignKey(Address)
    estd = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    courses = models.ManyToManyField(Course)
    rating = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.full_name

