from django.shortcuts import render
from .utils import get_event_title, get_event_names
from django.views.decorators.cache import cache_page


@cache_page(60 * 4.2)
def events_with_subscriptions(request, event_id):
    title = get_event_title(event_id)
    names = get_event_names(event_id)

    events_with_names_dict = {
        "id": event_id,
        "title": title,
        "names": names
    }

    return render(request, 'events_with_subscriptions.html',
                  {'events_with_names_dict': events_with_names_dict})
