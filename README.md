# MIT REX iCalendar

A calendar for events at MIT's [**R**esidence **EX**ploration](https://dormcon.mit.edu/rex/).

I wrote this in 30 minutes. Done this same song and dance so many times I can do it with my eyes closed. Maybe I should make an


Based on:
- https://rex.mit.edu/
- https://github.com/mit-dormcon/t-rex
- https://dormcon.mit.edu/rex/events/


## Deploy
```bash
poetry install
# For the lazy...
python3 main.py 
# For the more upstanding
gunicorn 'rex_ical:create_app()'
```

## Screenshots

Index of web server:
![Simplistic webpage with following text: "MIT REX iCalendar. Based on: T-REX, the DormCon REX API; REX Events on MIT DormCon. Cop it! How do I import this into Google Calendar?"](screenshots/webpage.png)

Generated calendar imported into Google Calendar:
![Four-day calendar from August 26th through 29th filled with dozens of events in small, overlapping cyan rectangles](screenshots/gcal.png)
