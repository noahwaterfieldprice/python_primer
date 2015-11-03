# Exercise 4.3
# Author: Noah Waterfield Price

import sys
try:
    F = float(sys.argv[1])
except IndexError:
    print 'You failed to provide a temperature in Fahrenheit '\
        'as input on the command line!'
    sys.exit(1)  # abort
C = 5. / 9 * (F - 32)
print "%g Fahrenheit = %g Celsius" % (F, C)

"""
Sample run:
python f2c_cml_exc.py
You failed to provide a temperature in Fahrenheit as input on the command line!
ython f2c_cml_exc.py 243
243 Fahrenheit = 117.222 Celsius
"""
