from django.contrib import admin
from event.models import EventType, SubEvent, Event

class EventTypeAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug':('name',)}

class SubEventAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields = {'slug':('name',)}

class EventAdmin(admin.ModelAdmin):
    list_display=('show', 'name', 'college', 'start')
    list_display_links = ['name']
    list_editable = ['show']
    list_filter = ['show', 'host_on_cdi', 'privacy', 'start']
    search_fields = ['name', 'tagline', 'description']


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(SubEvent, SubEventAdmin)
admin.site.register(Event, EventAdmin)
