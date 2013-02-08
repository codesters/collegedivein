from django import forms

from college.models import College, Course
from student.models import Student

q1 = College.objects.all()
q2 = Course.objects.all()

class SignupForm(forms.Form):
    college = forms.ModelChoiceField(queryset=q1, empty_label=None)
    course = forms.ModelChoiceField(queryset=q2, empty_label=None)

    def save(self, user):
        student = Student()
        student.user= user
        student.course = self.cleaned_data['college']
        student.college = self.cleaned_data['course']
        student.save()

