# Exercise 1.3
# Author: Noah Waterfield Price

seconds = raw_input('Type number of seconds to be converted to years\n')
years = float(seconds) / (365.25 * 24 * 60 * 60)
print "%.2f years" % (years)

"""
Sample run:
python seconds2years.py
Type number of seconds to be converted to years
1e9
31.69 years
"""
