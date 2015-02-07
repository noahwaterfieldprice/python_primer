# Exercise 8.15
from random import randint


def exact_frequencies():
    frequencies = {}
    for s in range(2, 13):
        frequency = 0
        for d1 in range(1, 7):
            for d2 in range(1, 7):
                if d1 + d2 == s:
                    frequency += 1
        frequencies[s] = frequency
    return frequencies


def calc_frequencies(N):
    frequencies = {i: 0 for i in range(2, 13)}
    for exp in range(N):
        d1, d2 = randint(1, 6), randint(1, 6)
        frequencies[d1 + d2] += 1
    frequencies = {i: j * 36 / float(N) for (i, j) in frequencies.iteritems()}
    return frequencies

exact_frequencies = exact_frequencies()
approx_frequencies = calc_frequencies(1000000)

length = 97
print '=' * length
header = '%-20s' % 'Sum of eyes'
header += '%7s' * 11 % tuple(range(2, 13))
print header
print '-' * length
line1 = '%-20s' % 'Approx. frequencies'
line1 += '%7.3f' * 11 % tuple([f for f in approx_frequencies.itervalues()])
print line1
line2 = '%-20s' % 'Exact frequencies'
line2 += '%7.0f' * 11 % tuple([f for f in exact_frequencies.itervalues()])
print line2
print '=' * length

"""
Sample run:
python freq_2dice.py
=================================================================================================
Sum of eyes               2      3      4      5      6      7      8      9     10     11     12
-------------------------------------------------------------------------------------------------
Approx. frequencies   0.995  1.988  2.981  4.006  5.012  6.004  5.005  4.003  3.003  1.999  1.003
Exact frequencies         1      2      3      4      5      6      5      4      3      2      1
=================================================================================================
"""
