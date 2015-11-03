# Exercise 4.8
# Author: Noah Waterfield Price

import sys
g = 9.81
try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    print 'Both v0 and t must be supplied on the command line'
    v0 = float(raw_input('v0 = ?\n'))
    t = float(raw_input('t = ?\n'))
except ValueError:
    print 'v0 and t must be pure numbers'
    sys.exit(1)

y = v0 * t - 0.5 * g * t ** 2
print y

"""
Sample run:
python ball_cml_qa.py
Both v0 and t must be supplied on the command line
v0 = ?
6
t = ?
4
-54.48
python ball_cml_qa.py 3 fw
v0 and t must be pure numbers
python ball_cml_qa.py 6 4
-54.48
"""
