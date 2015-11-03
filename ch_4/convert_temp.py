# Exercise 4.16
# Author: Noah Waterfield Price

def C2F(C):
    F = 9. / 5 * C + 32
    return F


def F2C(F):
    C = 5. / 9 * (F - 32)
    return C


def C2K(C):
    K = C + 273.15
    return K


def K2C(K):
    C = K - 273.15
    return C


def F2K(F):
    K = F2C(F) + 273.15
    return K


def K2F(K):
    F = C2F(K - 273.15)
    return F

if __name__ == '__main__':
    K = 0
    print 'Absolute zero = %g K, %g C, %g F' % (K, K2C(K), K2F(K))
    C = 0
    print 'Freezing point of water = %g K, %g C, %g F' % (C2K(C), C, C2F(C))
    F = 0
    print 'Freezing point of brine = %g K, %g C, %g F' % (F2K(F), F2C(F), F)

"""
Sample run:
python convert_temp.py
Absolute zero = 0 K, -273.15 C, -459.67 F
Freezing point of water = 273.15 K, 0 C, 32 F
Freezing point of brine = 255.372 K, -17.7778 C, 0 F
"""
