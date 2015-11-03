# Exercise 4.5
# Author: Noah Waterfield Price

import sys
val = eval(sys.argv[1])
print '%s is a Python %s object' % (val, type(val))

"""
Sample run:
python objects_cml.py 1
1 is a Python <type 'int'> object
python objects_cml.py 1.0
1.0 is a Python <type 'float'> object
python objects_cml.py 1 + 1j
(1 + 1j) is a Python <type 'complex'> object
python objects_cml.py [1,2]
[1,2] is a Python <type 'list'> object
python objects_cml.py (1,2)
(1,2) is a Python <type 'tuple'> object
python objects_cml.py "'hello'"
hello is a Python <type 'string'> object
"""
