from django.contrib import admin
from event.models import EventType, SubEvent, Event, Address

class EventTypeAdmin(admin.ModelAdmin):
    list_display=('name',)

class SubEventAdmin(admin.ModelAdmin):
    list_display=('name',)

class AddressAdmin(admin.ModelAdmin):
    list_display=('street', 'city')

class EventAdmin(admin.ModelAdmin):
    list_display=('name', 'college')


admin.site.register(EventType, EventTypeAdmin)
admin.site.register(SubEvent, SubEventAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Event, EventAdmin)
