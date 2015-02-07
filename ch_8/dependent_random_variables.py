# Exercise 8.22
from random import randint, random


def independent_random_variables(N):
    r = []
    for i in range(N):
        r.append(str(randint(0, 1)))
    return r


def dependent_random_variables(p, N):
    r = [str(randint(0, 1))]
    for i in range(N - 1):
        q = random()
        if q < p:
            r.append(r[i])
        elif q >= p:
            r.append(str((int(r[i]) + 1) % 2))
    return r


def compare_sequences(p, N):
    ri = independent_random_variables(N)
    rd = dependent_random_variables(p, N)
    print 'N = %d, p = %.1f' % (N, p)
    print 'Independent: ' + ''.join(ri)
    print 'Dependent:   ' + ''.join(rd)

N = 80
for p in (0.5, 0.8, 0.9):
    compare_sequences(p, N)

"""
Sample run:
python dependent_random_variables.py
N = 80, p = 0.5
Independent: 01010110000000011000100011001101101110000000010111001001011111010001111110101101
Dependent:   11111101000110010011100110100011101100000110001000010111000001111111110101111010
N = 80, p = 0.8
Independent: 00100101001001110111100100011101001001110111111000101010000010111110101000001000
Dependent:   11111111000011111110000111111111111000101111100001111111111100000000001111110011
N = 80, p = 0.9
Independent: 01100000111111110101101111010111111110101100010101000101110111101101000010010100
Dependent:   00000000011111111111110110000000000000000000000000000000111111111100000000000000
"""
