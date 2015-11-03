# Exercise 4.19
# Author: Noah Waterfield Price

from math import sin, pi
import sys
from sinesum2 import S, f, table
_filname = sys.argv[0]
_usage = """ % _filname
Usage: %s '[1, 3, 75, 10, 30, 100]' '[0.01, 0.25, 0.49]' 2*pi
Computes the sine sum approximation of a piecewise constant 
function. Takes n list, alpha list and function domain.
"""

if len(sys.argv) < 4:
    print _usage
    raise IndexError(
        'Domain, n list and alpha list must be given on command-line')
n_list = eval(sys.argv[1])
alpha_list = eval(sys.argv[2])
T = eval(sys.argv[3])
table(n_list, alpha_list, T)

"""
Sample run:
python sinesum1.py '[1, 3, 75, 10, 30, 100]' '[0.01, 0.25, 0.49]' 2*pi
n = 1
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.1595792 0.0000000 -0.1595792
     Error 0.8404208 0.8404208 0.8404208

n = 3
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.4654944 0.0000000 -0.4654944
     Error 0.5345056 0.5345056 0.5345056

n = 5
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.7336510 0.0000000 -0.7336510
     Error 0.2663490 0.2663490 0.2663490

n = 10
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 1.1349367 0.0000000 -1.1349367
     Error 0.1349367 0.1349367 0.1349367

n = 30
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.9648738 0.0000000 -0.9648738
     Error 0.0351262 0.0351262 0.0351262

n = 100
  Function t=0.01*pi t=0.25*pi t=0.49*pi
   f(t, T) 1.0000000 0.0000000 -1.0000000
S(t, n, T) 0.9746817 0.0000000 -0.9746817
     Error 0.0253183 0.0253183 0.0253183
"""
