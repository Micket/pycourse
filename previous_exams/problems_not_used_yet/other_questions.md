
Question example (6pt)
================

When writing a calendar/team-planning application, you get to the point of supporting appointments.

Part A (4pt)
------
Implement a superclass `Appointment` and subclasses `Onetime`, `Daily`, `Monthly`.
An appointment has a description (for example "see the dentist") and a date.
Write the methods:

 * `occurs_on(year, month, day)` that checks whether the appointment occurs on that date
 * `next_occurence(year, month, day)` that returns the date of the next time the appointment occurs (or None), *after* the specified date.

Make a short list of various appointments and try it out for a few dates.


Part B (2pt)
------

Add a method `save(file)` that saves the files contents to an (already opened) file descriptor.

The following should work:
```python
with open('calendar.data') as f:
    for appointment in appointments:
        appointment.save(f)
```
The data should be stored as XML-tags, for example a monthly meeting with the study group would be:
```
<appointment type="monthly" date="2015-04-13">
Study group meetup
</appointment>
```
