# Exercise 6.12
# Author: Noah Waterfield Price

infile = open('stars.dat', 'r')
data = {}
for line in infile.readlines()[1:]:
    words = line.split()
    name = ' '.join(words[:-3])
    luminosity = float(words[-1])
    data[name] = luminosity

print '='*31
print '%-20s %10s' % ('Star', 'Luminosity')
print '-'*31
for star, luminosity in data.iteritems():
    print '%-20s %10.5f' % (star, luminosity)
print '='*31


"""
Sample run:
python stars_data_dict1.py
===============================
Star                 Luminosity
-------------------------------
Wolf 359                0.00002
Sun                     1.00000
Alpha Centauri C        0.00006
Alpha Centauri B        0.45000
Alpha Centauri A        1.56000
Luyten 726-8 A          0.00006
Sirius B                0.00300
Sirius A               23.60000
Luyten 726-8 B          0.00004
BD +36 degrees 2147     0.00600
Barnard's Star          0.00050
Ross 154                0.00050
===============================
"""
