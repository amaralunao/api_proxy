import requests

from .constants import HOST, API_TOKEN, headers


def get_event(event_id):
    url = HOST+"events/{EVENT_ID}/".format(EVENT_ID=event_id)
    return requests.get(url, headers=headers).json()


def get_event_subscriptions(event_id):
    url = HOST+"event-subscriptions/?event_ids=[{EVENT_ID}]".format(EVENT_ID=event_id)
    return requests.get(url, headers=headers).json()


def get_event_title(event_id):
    event_details = get_event(event_id)
    if event_details.get('error'):
        title = "Error occured while getting the title"
    title = event_details.get('data')[0].get('title')
    return title


def get_event_names(event_id):
    event_details = get_event_subscriptions(event_id)
    if event_details.get('error'):
        names = ['Error occured while getting the event names']
    else:
        names = []
        for entry in event_details.get('data'):
            names.append(str(entry.get('subscriber').get('first_name')))

    return names
