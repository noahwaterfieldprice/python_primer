# Exercise 4.12
# Author: Noah Waterfield Price

import sys
import datetime

try:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
except IndexError:
    print 'Year, month and day must be supplied on the command line'
    sys.exit(1)
except ValueError:
    print 'Year, month and day must be integers'
    sys.exit(1)
if month < 1 or month > 12:
    raise ValueError('Month must be between 1 and 12')
if day < 1 or day > 31:
    raise ValueError('Day must be between 1 and 31')

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
day = datetime.date(year, month, day).weekday()

print days[day]
