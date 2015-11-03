# Exercise 4.14
# Author: Noah Waterfield Price

import sys
from math import *

try:
    i1 = eval(sys.argv[1])
    i2 = eval(sys.argv[2])
except IndexError:
    print 'i1 and i2 must be given on the command line'
    sys.exit(1)

r = i1 + i2
print '%s + %s becomes %s\nwith value %s' % \
      (type(i1), type(i2), type(r), r)

"""
Sample run:
python add_cml2.py 'sqrt(2)' 'sin(1.2)'
<type 'float'> + <type 'float'> becomes <type 'float'>
with value 2.34625264834
"""
