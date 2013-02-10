from django.contrib import admin
from college.models import Course, College, Address

class CollegeAdmin(admin.ModelAdmin):
    list_display=('name', 'college_type', 'website')

class AddressAdmin(admin.ModelAdmin):
    list_display=('street', 'city')


admin.site.register(Course)
admin.site.register(College, CollegeAdmin)
admin.site.register(Address, AddressAdmin)
