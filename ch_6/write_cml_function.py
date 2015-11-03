# Exercies 6.19
# Author: Noah Waterfield Price

from numpy import *
from scitools.StringFunction import StringFunction
import sys

try:
    f = StringFunction(sys.argv[1])
    a = float(eval(sys.argv[2]))
    b = float(eval(sys.argv[3]))
    n = int(sys.argv[4])
except IndexError:
    print 'f, a, b and n mus be provided on the command line'
    sys.exit(1)

outfile = open('write_cml_function.txt', 'w')
x = linspace(a, b, n)
f.vectorize(globals())
for xi, fi in zip(x, f(x)):
    outfile.write('%14.8f %14.8f\n' % (xi, fi))
outfile.close()
