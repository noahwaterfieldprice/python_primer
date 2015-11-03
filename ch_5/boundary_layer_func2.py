# Exercise 5.41
# Author: Noah Waterfield Price

import numpy as np
import matplotlib.pyplot as plt
import math


def v(x, mu=1E-6, exp=math.exp):
    x = np.float128(x)
    mu = np.float128(mu)
    numerator = 1 - exp(x / mu)
    denominator = 1 - exp(1 / mu)
    return numerator, denominator, numerator / denominator

for x in np.linspace(0, 1, 11):
    for exp, mod in [(math.exp, 'math'), (np.exp, 'numpy')]:
        print mod
        try:
            print v(x, 0.001, exp=exp)
        except:
            print 'Error'

x = np.linspace(0, 1, 1001)
for mu in [1, 0.01, 0.001]:
    a, b, vel = v(x, mu, np.exp)
    plt.plot(x, vel)
    plt.xlabel('x')
    plt.ylabel('velocity')
    plt.show()


"""
Sample run:
python boundary_layer_func2.py
...
math
Error
numpy
(0.0, -1.9700711140170059836e+434, -0.0)
math
Error
numpy
(-2.6881171418161447748e+43, -1.9700711140170059836e+434, 1.3644772123657158996e-391)
math
Error
numpy
(-7.2259737681257993986e+86, -1.9700711140170059836e+434, 3.6678745841777890175e-348)
math
Error
numpy
(-1.9424263952413300672e+130, -1.9700711140170059836e+434, 9.8596765437603523859e-305)
math
Error
numpy
(-5.2214696897642164128e+173, -1.9700711140170059836e+434, 2.6503965530044027703e-261)
math
Error
numpy
(-1.4035922178528228016e+217, -1.9700711140170059836e+434, 7.1245764067413596862e-218)
math
Error
numpy
(-3.7730203009302278098e+260, -1.9700711140170059836e+434, 1.9151695967141917432e-174)
...
"""
