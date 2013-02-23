from django.contrib import admin
from college.models import Course, CollegeType, College, Address

class CourseAdmin(admin.ModelAdmin):
    list_display=('name', 'duration')
    prepopulated_fields = {'slug':('name',)}

class CollegeAdmin(admin.ModelAdmin):
    list_display=('name', 'college_type', 'website')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name', 'about']

class AddressAdmin(admin.ModelAdmin):
    list_display=('street', 'city')

class CollegeTypeAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Course, CourseAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(CollegeType, CollegeTypeAdmin)
admin.site.register(Address, AddressAdmin)
