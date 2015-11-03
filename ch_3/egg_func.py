# Exercise 3.15
# Author: Noah Waterfield Price

from math import log, pi


def egg(M, T_0, T_y):
    rho = 1.038 * 1000  # Egg density (kg m^-3_
    c = 3.7 * 1000  # Specific heat capacity (J kg^-1 K^-1)
    K = 0.54  # Thermal conductivity (W m^-1 K^-1)
    T_w = 373.15  # Boiling water temperature (K)
    t = M ** (2.0 / 3) * c * rho ** (1.0 / 3) / \
        (K * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * \
        log(0.76 * (T_0 - T_w) / (T_y - T_w))
    return t

# Egg from fridge
T_0 = 277.15
# Soft boiled
T_y = 63 + 273.15
# Small egg
M = 0.047
t_small = egg(M, T_0, T_y)
# Large egg
M = 0.067
t_large = egg(M, T_0, T_y)
print 'From the fridge: to soft boil a small egg cook for %.2f minutes \
and a large egg for %.2f minutes.' % (t_small / 60, t_large / 60)

# Hard boiled
T_y = 70 + 273.15
# Small egg
M = 0.047
t_small = egg(M, T_0, T_y)
# Large egg
M = 0.067
t_large = egg(M, T_0, T_y)
print 'From the fridge: to hard boil a small egg cook for %.2f minutes \
and a large egg for %.2f minutes.' % (t_small / 60, t_large / 60)

# Egg at room temperature
T_0 = 293.15
# Soft boiled
T_y = 63 + 273.15
# Small egg
M = 0.047
t_small = egg(M, T_0, T_y)
# Large egg
M = 0.067
t_large = egg(M, T_0, T_y)
print 'At room temperature: to soft boil a small egg cook for %.2f minutes \
and a large egg for %.2f minutes.' % (t_small / 60, t_large / 60)

# Hard boiled
T_y = 70 + 273.15
# Small egg
M = 0.047
t_small = egg(M, T_0, T_y)
# Large egg
M = 0.067
t_large = egg(M, T_0, T_y)
print 'At room temperature: to hard boil a small egg cook for %.2f minutes \
and a large egg for %.2f minutes.' % (t_small / 60, t_large / 60)

"""
Sample run:
python egg_func.py
From the fridge: to soft boil a small egg cook for 3.99 minutes and a large egg for 5.05 minutes.
From the fridge: to hard boil a small egg cook for 5.22 minutes and a large egg for 6.61 minutes.
At room temperature: to soft boil a small egg cook for 2.92 minutes and a large egg for 3.69 minutes.
At room temperature: to hard boil a small egg cook for 4.15 minutes and a large egg for 5.25 minutes.
"""
