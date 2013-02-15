from django.contrib import admin
from event.models import EventType, SubEvent, Event

class EventTypeAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug':('name',)}

class SubEventAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
    list_display=('name', 'college')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(SubEvent, SubEventAdmin)
admin.site.register(Event, EventAdmin)
