Simple Api Proxy
================

Steps taken and tools used
--------------------------

* Decided to use Atom editor and Django==1.9.7
* Initialized my git repository and Django project skeleton
* Testing the API calls was done via Postman(Chrome extension)
* I decided to look for an alternative to get the desired data and found an
  easy and elegant way to do so with: Requests: HTTP for Humans = > created
  4 simple functions to retrieve the event, event_subscription, title and names
  and put these functions in an utils.py.
* Since the HOST, API Token and Header format are constants for this API Proxy,
  I decided to put these in a constants.py and to import them to my utils.py
  module.
* Looked into caching on the Django documentation site and found the simple
  per-view caching to which I could pass the results caching time of 4.2 minutes
  (60 * 4.2)
* Wrote the function view events_with_subscriptions that uses the utils
  functions to retrieve and render the data with help from a basic html template 
* Also included the url for the final api call based on the view and with
  matching the event_id by using regex
* It did not seem necessary to store the data by using a model in the database
* Created a requirements.txt to include django and requests.
* Did not create any tests 
