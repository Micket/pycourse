# A few comments:
# After testing the implementation, i realize i should have revealed a bit of useful components in
# the  "datetime" module.
# This is particularly important for the "nextOccurrence" method (that the book didn't include).
#
# It also wasn't very logical to have a monthly appointment, as the months don't all have the same number of days
# (I somehow missed this when i thought up the question), so I switched this for a weekly appointment instead.
#
# It should also have been worth more points (perhaps 8p) on an exam, instead of the (6p) i wrote on the question.
#
#   / Mikael

import datetime


class Appointment:
    def __init__(self, description, date):
        """
        Constructor for appointments, storing the description and starting date.
        """
        self.description = description
        self.date = date

    def occurs_on(self, date):
        """
        Checks if the appointment occurs on the given date
        """
        raise NotImplementedError("Missing 'occursOn' implementation in appointment")

    def next_occurrence(self, date):
        """
        Returns the date of the next occurrence if any, otherwise None
        """
        raise NotImplementedError("Missing 'nextOccurrence' implementation in appointment")

    def save(self, fid):
        """
        Saves the file to the descriptor
        """
        date = "{}-{}-{}".format(self.date.year, self.date.month, self.date.day)
        fid.write('<Appointment type="{}", date="{}">\n'.format(self.type, date))
        fid.write(self.description + '\n')
        fid.write('</Appointment>\n'.format(type))


class OneTime(Appointment):
    type = 'onetime'

    def occurs_on(self, date):
        return date == self.date

    def next_occurrence(self, date):
        if date <= date:
            return self.date


class Daily(Appointment):
    type = 'daily'

    def occurs_on(self, date):
        return date >= self.date

    def next_occurrence(self, date):
        if date <= self.date:
            return date
        else:
            return date + datetime.timedelta(days=1)


class Weekly(Appointment):
    type = 'weekly'

    def occurs_on(self, date):
        if date >= self.date:
            return self.date.weekday() == date.weekday()

    def next_occurrence(self, date):
        if date <= self.date:
            return self.date
        else:
            return date + datetime.timedelta(days=7)


# Testing part A:
appointments = [OneTime('Wedding', datetime.date(2015, 4, 10)),
                Daily('Bachelor thesis group meeting', datetime.date(2015, 1, 20)),
                Weekly('Ninja practice', datetime.date(2014, 1, 1))]

for appointment in appointments:
    d = datetime.date(2015, 3, 5)
    occurs = appointment.occurs_on(d)
    print("'{}' {} occurs on {}".format(appointment.description,
                                        'does' if occurs else "doesn't",
                                        d))
    if not occurs:
        next_d = appointment.next_occurrence(d)
        if next_d is not None:
            print("It will occur next on {}".format(next_d))


# Testing part B:
with open('calendar.data', 'w') as f:
    for appointment in appointments:
        appointment.save(f)

