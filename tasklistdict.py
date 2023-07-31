"""Module to print a tasklist based on the day of the week."""

import datetime

#get current weekday
dt = datetime.datetime.today()
x = dt.isoweekday()

#tasklist dict
taskdict = dict(
    Monday = "MONDAY\n\n• Dishes\n• Shower",
    Tuesday = "TUESDAY\n\n• Tidy my side of the room (30 minutes)\n• Shower",
    Wednesday = "WEDNESDAY\n\n• Tidy the living room (30 minutes)\n• Shower",
    Thursday = "• THURSDAY\n\n• Shower",
    Friday = "FRIDAY \n\n• Shower",
    Saturday = "SATURDAY \n\n• Tidy the kitchen\n• Shower",
    Sunday = "SUNDAY\n\n• Laundry \n• 30 minute general tidy \n•Shower"
,)

#printing dict messages by day of the week
if x == 1:
    print(taskdict["Monday"])
elif x == 2:
    print(taskdict["Tuesday"])
elif x == 3:
    print(taskdict["Wednesday"])
elif x == 4:
    print(taskdict["Thursday"])
elif x == 5:
    print(taskdict["Friday"])
elif x == 6:
    print(taskdict["Saturday"])
elif x == 7:
    print(taskdict["Sunday"])
