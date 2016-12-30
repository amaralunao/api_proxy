from django.conf.urls import url
from .views import events_with_subscriptions

urlpatterns = [
    url(r'^events-with-subscriptions/(?P<event_id>[0-9a-fA-F_]+)/*',
        events_with_subscriptions, name='events-with-subscriptions'),
        ]
