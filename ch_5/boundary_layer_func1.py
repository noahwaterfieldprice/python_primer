# Exercise 5.40
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import math


def v(x, mu=1E-6, exp=math.exp):
    numerator = 1 - exp(x / mu)
    denominator = 1 - exp(1 / mu)
    return numerator, denominator, numerator / denominator

for x in np.linspace(0, 1, 21):
    for exp, mod in [(math.exp, 'math'), (np.exp, 'numpy')]:
        print mod
        try:
            print v(x, 0.001, exp=exp)
        except:
            print 'Error'

x = np.linspace(0, 1, 1001)

for mu in (1, 0.01, 0.001):
    a, b, vel = v(x, mu, np.exp)
    plt.plot(x, vel)
    plt.xlabel('x')
    plt.ylabel('velocity')
    plt.show()

"""
Sample run:
python boundary_layer_func1.py
math
Error
numpy
/Users/Noah/dev/apospwp/ch_5/boundary_layer_func1.py:8: RuntimeWarning: overflow encountered in exp
  denominator = 1 - exp(1 / mu)
(0.0, -inf, -0.0)
math
Error
numpy
(-5.184705528587072e+21, -inf, 0.0)
math
Error
numpy
(-2.6881171418161356e+43, -inf, 0.0)
math
Error
numpy
(-1.3937095806664192e+65, -inf, 0.0)
...
...
"""
