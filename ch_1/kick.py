# Exercise 1.11
# Author: Noah Waterfield Price

from math import pi

C_D = 0.2  # Drag coefficient
rho = 1.2  # Density of air (kg m^-3)
A = pi * 0.11 ** 2  # Football cross sectional area (m^2)
m = 0.43  # Football mass (kg)
g = 9.81  # Gravitational acceleration (ms^-1)

F_g = m * g

speed_conversion = 1000.0 / 3600

V = 120 * speed_conversion  # Hard kick velocity (m/s)
F_d = 0.5 * C_D * rho * A * V ** 2
print 'For a hard kick (v = %g), the gravitational force is %g and \
    the drag force is %g' % (V, F_g, F_d)

V = 10 * speed_conversion  # Soft kick velocity (m/s)
F_d = 0.5 * C_D * rho * A * V ** 2
print 'For a soft kick (v = %g), the gravitational force is %g and \
the drag force is %g' % (V, F_g, F_d)

"""
Sample run:
python kick.py
For a hard kick (v = 33.3333), the gravitational force is 4.2183 and the drag force is 5.06844
For a soft kick (v = 2.77778), the gravitational force is 4.2183 and the drag force is 0.0351975
"""
