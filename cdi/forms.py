from django.forms import ModelForm
from django.contrib.auth.models import User
from student.models import Student

class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name')

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields = ('phone', 'college', 'course', 'batch_start_year')
