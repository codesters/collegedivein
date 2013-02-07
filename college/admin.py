from django.contrib import admin
from college.models import Course, College

class CollegeAdmin(admin.ModelAdmin):
    list_display=('name', 'college_type', 'website')


admin.site.register(Course)
admin.site.register(College, CollegeAdmin)
