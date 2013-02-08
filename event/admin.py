from django.contrib import admin
from event.models import EventType, SubEvent, Event

class EventTypeAdmin(admin.ModelAdmin):
    list_display=('name',)

class SubEventAdmin(admin.ModelAdmin):
    list_display=('name',)

class SponsorAdmin(admin.ModelAdmin):
    list_display=('name', 'website')

class EventAdmin(admin.ModelAdmin):
    list_display=('name', 'host')


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(SubEvent, SubEventAdmin)
admin.site.register(Event, EventAdmin)
