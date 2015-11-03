# Exercise 4.15
# Author: Noah Waterfield Price

import sys

try:
    C = float(sys.argv[1])
except IndexError:
    print 'C must be provided as a command-line argument'
    sys.exit(1)
except ValueError:
    print 'C must be a pure number'
    sys.exit(1)

"""
Sample run:
python cml_exception.py
C must be provided as a command-line argument
python cml_exception.py a
C must be a pure number
python cml_exception.py 3
"""
