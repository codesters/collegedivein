from django.db import models

STATES = (
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('Punjab','Punjab'),
    ('Haryana','Haryana'),
    ('Delhi','Delhi'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Assam','Assam'),
    ('Meghalaya','Meghalaya'),
    ('Manipur','Manipur'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Sikkim','Sikkim'),
    ('Tripura','Tripura'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('West Bengal','West Bengal'),
    ('Rajasthan','Rajasthan'),
    ('Gujarat','Gujarat'),
    ('Maharashtra','Maharashtra'),
    ('Goa','Goa'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Orissa','Orissa'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Andhra Pradesh', 'Andhra Pradesh')
)

COLLEGE_TYPE = (
    ('Arts/Commerce/Science', 'Arts/Commerce/Science'),
    ('Engineering', 'Engineering'),
    ('Management', 'Management'),
    ('Law', 'Law'),
    ('Medical/Dental', 'Medical/Dental'),
    ('University', 'University'),
    ('Others', 'Others')
    )


class Course(models.Model):

    name = models.CharField(max_length=60)
    full_name = models.CharField(max_length = 300)
    duration = models.SmallIntegerField(default=3)

    def __unicode__(self):
        return self.name

class College(models.Model):

    name=models.CharField(max_length=300)
    full_name = models.CharField(max_length=300)
    college_type=models.CharField(max_length = 40, choices = COLLEGE_TYPE)
    add_street = models.CharField(max_length=350, blank=True, default='')
    add_city = models.CharField(max_length=100, default='New Delhi')
    add_state = models.CharField(max_length=40, choices=STATES)
    add_pincode = models.PositiveIntegerField(blank=True, null=True)
    about = models.TextField(default = '')
    estd = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    courses = models.ManyToManyField(Course)
    rating = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return self.name

