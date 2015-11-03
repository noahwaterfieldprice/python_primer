# Exercise 6.10
# Author: Noah Waterfield Price

def read_densities_v1(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities


def read_densities_v2(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substance = ' '.join(words[:-1])
        densities[substance] = density
    infile.close()
    return densities


def read_densities_v3(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substance = line[:12].strip()
        densities[substance] = density
    infile.close()
    return densities

f = 'densities.dat'
print read_densities_v1(f) == read_densities_v2(f) == read_densities_v3(f)

"""
Sample run:
python density_improved.py
True
"""
