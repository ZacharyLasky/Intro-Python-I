"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

inp1 = input('Enter date: MM/YYYY: ')
curMonth = datetime.today().month


def cal(userInp):
    if len(userInp) == 0:
        print(calendar.TextCalendar().formatmonth(2019, curMonth))
    elif len(userInp) <= 2:
        print(calendar.TextCalendar().formatmonth(2019, int(userInp)))
    elif len(userInp) >= 6:
        userDate = inp1.split('/')
        date = userDate[0]
        year = userDate[1]
        print(calendar.TextCalendar().formatmonth(int(year), int(date)))
    else:
        print("please print format mm/yyyy")


cal(inp1)
