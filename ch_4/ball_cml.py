# Exercise 4.7
# Author: Noah Waterfield Price

import argparse
g = 9.81

parser = argparse.ArgumentParser()

parser.add_argument('--v0', '--initial_velocity', type=float,
                    default=0.0, help='initial velocity', metavar='v')
parser.add_argument('--t', '--time', type=float, default=1.0,
                    help='time', metavar='t')
args = parser.parse_args()

y = args.v0 * args.t - 0.5 * g * args.t ** 2
print y

"""
Sample run:
python ball_cml.py --v0 10 --t 4
-38.48
"""
