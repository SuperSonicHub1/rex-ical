from requests import Session
from icalendar import Calendar, Event
from datetime import datetime
from typing import TypedDict, List, Dict, Optional

class TRexAPIColors(TypedDict):
	dorms: Dict[str, str]
	tags: Dict[str, str]

class TRexEvent(TypedDict):
	name: str
	dorm: str
	location: str
	start: str
	end: str
	description: str
	tags: List[str]
	group: Optional[str]

class TRexAPIResponse(TypedDict):
	"""
	https://github.com/mit-dormcon/website/blob/master/components/t-rex/types.ts
	"""
	#  The title of the current experience, such as "REX 2023"
	name: str
	# ISO Date string of when the current JSON of events was published
	published: str
	events: List[TRexEvent]
	dorms: List[str]
	tags: List[str]
	# Maps event properties to background colors
	colors: TRexAPIColors
	start: str
	end: str

session = Session()

def rex_events() -> TRexAPIResponse:
	res = session.get('https://rex.mit.edu/api.json')
	res.raise_for_status()
	return res.json()

def create_event(event: TRexEvent) -> Event:
	event_ical = Event()

	datetime_start = datetime.fromisoformat(event['start'])
	datetime_end = datetime.fromisoformat(event['end'])
	event_ical.add("dtstart", datetime_start)
	event_ical.add("dtend", datetime_end)

	event_ical.add("location", event['location'])

	event_ical.add("summary", event['name'])
	event_ical.add("description", event['description'])
	event_ical.add("uid", ':'.join([event['name'], event['start']]))

	event_ical.add('categories', event['tags'])
	event_ical.add('organizer', event['dorm'])

	return event_ical

def get_calendar() -> Calendar:
	events = rex_events()

	cal = Calendar()
	cal.add('prodid', '-//KAWCCO (@supersonichub1)/EN')
	cal.add('version', '2.0')
	cal.add("method", "PUBLISH")
	cal.add('name', events['name'])
	cal.add('last-modified', datetime.fromisoformat(events['published']))

	for event in (create_event(event) for event in events['events']):
		cal.add_component(event)

	return cal
