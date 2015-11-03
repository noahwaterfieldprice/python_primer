# Exercise 6.13
# Author: Noah Waterfield Price

infile = open('stars.dat', 'r')
data = {}
for line in infile.readlines()[1:]:
    words = line.split()
    name = ' '.join(words[:-3])
    if words[-3] == '-':
        distance = '-'
        apparent_brightness = '-'
    else:
        distance = float(words[-3])
        apparent_brightness = float(words[-2])
    luminosity = float(words[-1])
    data[name] = {'distance': distance,
                  'apparent brightness': apparent_brightness,
                  'luminosity': luminosity}

print '='*68
print '%-20s %12s %18s %15s' % ('Star', 'Distance',
                                'App. brightness', 'Luminosity')
print '-'*68
for star in data:
    if star == 'Sun':
        print '%-20s %12s %18s %15.5f' % (star,
                                          data[star]['distance'],
                                          data[star]['apparent brightness'],
                                          data[star]['luminosity'])
    else:
        print '%-20s %12f %18f %15.5f' % (star,
                                          data[star]['distance'],
                                          data[star]['apparent brightness'],
                                          data[star]['luminosity'])
print '='*68

"""
Sample run:
python stars_data_dict2.py
====================================================================
Star                     Distance    App. brightness      Luminosity
--------------------------------------------------------------------
Wolf 359                 7.700000           0.000001         0.00002
Sun                             -                  -         1.00000
Alpha Centauri C         4.200000           0.000010         0.00006
Alpha Centauri B         4.300000           0.077000         0.45000
Alpha Centauri A         4.300000           0.260000         1.56000
Luyten 726-8 A           8.400000           0.000003         0.00006
Sirius B                 8.600000           0.001000         0.00300
Sirius A                 8.600000           1.000000        23.60000
Luyten 726-8 B           8.400000           0.000002         0.00004
BD +36 degrees 2147      8.200000           0.000300         0.00600
Barnard's Star           6.000000           0.000040         0.00050
Ross 154                 9.400000           0.000020         0.00050
====================================================================
===============================
"""
