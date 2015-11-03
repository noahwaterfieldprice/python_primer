# Exercise 4.20
# Author: Noah Waterfield Price

from math import sin, pi
from sinesum2 import table
import argparse
parser = argparse.ArgumentParser()


def evalcmlarg(text):
    return eval(text)

parser.add_argument(
    '--n', '--n_list', type=evalcmlarg, default='[1, 3, 5, 10, 30, 100]',
    help='List of n values')
parser.add_argument(
    '--alpha', '--alpha_list', type=evalcmlarg, default='[0.01, 0.25, 0.49]',
    help='List of alpa values')
parser.add_argument('--T', type=evalcmlarg, default='2*pi',
                    help='Domain of function')
args = parser.parse_args()

table(args.n, args.alpha, args.T)

"""
Sample run:
python sinesum4.py --n '[1, 3, 5, 10, 30, 100]' --alpha '[0.01, 0.25, 0.49]' --T 2*pi
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
