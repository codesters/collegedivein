from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('user', 'college', 'course')


admin.site.register(Student, StudentAdmin)
