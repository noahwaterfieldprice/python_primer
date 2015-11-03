# Exercise 4.10
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

if t < 0 or t > 2 * v0 / g:
    raise ValueError('t=%g is a non-physical value.'
                     'must be between 0 and 2v0/g' % t)
    sys.exit(1)

y = v0 * t - 0.5 * g * t ** 2
print y

"""
Sample run:
ppython ball_cml_errorcheck.py
Both v0 and t must be supplied on the command line
v0 = ?
6
t = ?
3
Traceback (most recent call last):
  File "ball_cml_errorcheck.py", line 16, in <module>
    'must be between 0 and 2v0/g' % t)
ValueError: t=3 is a non-physical value.must be between 0 and 2v0/g
python ball_cml_qa.py 3 fw
v0 and t must be pure numbers
python ball_cml_qa.py 6 1
1.095s
"""
