# Exercise 4.2
# Author: Noah Waterfield Price

import sys
F = float(sys.argv[1])
C = 5 / 9. * (F - 32)
print "%g Fahrenheit = %g Celsius" % (F, C)

"""
Sample run:
python f2c_cml.py 243
243 Fahrenheit = 117.222 Celsius
"""
