from math import log, pi

rho = 1.038*1000 # Egg density (kg m^-3_
c = 3.7*1000 # Specific heat capacity (J kg^-1 K^-1)
K = 0.54 # Thermal conductivity (W m^-1 K^-1)
T_w = 373.15 # Boiling water temperature (K)
T_y = 343.15 # Desired yolk temperature (K)

#Egg from fridge
T_0 = 277.15
#Small egg
M = 0.047 
t_small = M**(2.0/3)*c*rho**(1.0/3)/(K*pi**2*(4*pi/3)**(2.0/3))*log(0.76*(T_0 - T_w)/(T_y - T_w))
#Large egg
M = 0.067
t_large = M**(2.0/3)*c*rho**(1.0/3)/(K*pi**2*(4*pi/3)**(2.0/3))*log(0.76*(T_0 - T_w)/(T_y - T_w))
print 'From the fridge: to hard boil a small egg cook for %.2f minutes and a large egg for %.2f minutes.' % (t_small/60, t_large/60)

#Egg at room temperature
T_0 = 293.15
#Small egg
M = 0.047 
t_small = M**(2.0/3)*c*rho**(1.0/3)/(K*pi**2*(4*pi/3)**(2.0/3))*log(0.76*(T_0 - T_w)/(T_y - T_w))
#Large egg
M = 0.067
t_large = M**(2.0/3)*c*rho**(1.0/3)/(K*pi**2*(4*pi/3)**(2.0/3))*log(0.76*(T_0 - T_w)/(T_y - T_w))
print 'At room temperature: to hard boil a small egg cook for %.2f minutes and a large egg for %.2f minutes.' % (t_small/60, t_large/60)

"""
Sample run:
python egg.py
From the fridge: to hard boil a small egg cook for 5.22 minutes and a large egg for 6.61 minutes.
At room temperature: to hard boil a small egg cook for 4.15 minutes and a large egg for 5.25 minutes.
"""
	