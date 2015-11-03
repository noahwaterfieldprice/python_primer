# Exercise 1.4
# Author: Noah Waterfield Price"

inch = 0.0254
foot = inch * 12
yard = foot * 3
mile = yard * 1760

metres = raw_input(
    'Enter distance in meters to be converted to imperial units\n')
metres = float(metres)
inches = metres / inch
feet = metres / foot
yards = metres / yard
miles = metres / mile

print '{m:g} metres is equivalent to {i:g} inches, {f:g} feet, {y:g} yards,\
 {mi:g} miles.'.format(m=metres, i=inches, f=feet, y=yards, mi=miles)

"""
Sample run:
python python length_conversion.py
Enter distance in meters to be converted to imperial units
640
640 metres is equivalent to 25196.9 inches, 2099.74 feet, 699.913 yards, 0.397678 miles.
"""
