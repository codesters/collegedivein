from event.models import EventType

def navigation(request):
    event_types_list = EventType.objects.all().order_by('name')
    return {'EVENT_TYPES': event_types_list}
