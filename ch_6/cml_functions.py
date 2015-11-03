# Exercise 6.20
# Author: Noah Waterfield Price

import sys
from scitools.StringFunction import StringFunction

"""
Takes a function given on the command line and
evaluates it for a value also given on the command line
Args:
    - sys.argv[1]: function (string)
    - sys.argv[2]: independent variable (string)
    - sys.argv[3]: value for function to be evaluated at (float)
    - sys.argv[4]: value(s) of parametes in function (dict of floats)
Example: python snippet1.py 'a*sin(x)*exp(b*x**2)' x 2.12 {'a': 2, 'b':4}
"""
parameters = {}
for prm in sys.argv[4]:
    key, value = prm.split('=')
    parameters[key] = eval(value)
f = StringFunction(sys.argv[1],
                   independent_variables=sys.argv[2],
                   **parameters)
var = float(sys.argv[3])
print f(*var)  # Needed to add star for multiple arguments given as tuple


"""
Takes a function given on the command line and
evaluates it for a value also given on the command line
Args:
    - sys.argv[1]: function (string)
    - sys.argv[2]: independent variable (string)
    - sys.argv[3]: value for function to be evaluated at (float)
    - sys.argv[4:]: value(s) of parametes in function given in form a=2 b=4
Example: python snippet2.py 'a*sin(x)*exp(b*x**2)' x 2.12 a=2 b=4
"""
f = eval('StringFunction(sys.argv[1], ' +
         'independent_variables=sys.argv[2], %s)' %
         (', '.join((sys.argv[4:]))))
var = float(sys.argv[3])
print f(*var)
