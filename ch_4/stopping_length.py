# Exercise 4.11
# Author: Noah Waterfield Price

import sys
g = 9.81  # acceleration due to gravity

try:
    # initial velocity (convert to m/s)
    v0 = (1000. / 3600) * float(sys.argv[1])
    mu = float(sys.argv[2])  # coefficient of friction
except IndexError:
    print 'Both v0 (in km/s) and mu must be supplied on the command line'
    v0 = (1000. / 3600) * float(raw_input('v0 = ?\n'))
    mu = float(raw_input('mu = ?\n'))
except ValueError:
    print 'v0 and mu must be pure numbers'
    sys.exit(1)

d = 0.5 * v0 ** 2 / mu / g
print d

"""
Sample run:
python stopping_length.py 120 0.3
188.771850342
python stopping_length.py 50 0.3
32.7728906843
"""
