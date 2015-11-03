# Exercise 4.25
# Author: Noah Waterfield Price

from binomial_distribution import binomial

print 'What is the probability of gettinger two heads when \
flipping a coin 5 times?'
print '%.6f\n' % binomial(2, 5, 0.5)
print 'What is the probability of getting fours ones in a rown when \
throwing a die?'
print '%.6f\n' % binomial(4, 4, 1. / 6)
print 'What is the probability that a skier will experience a ski \
break during five\n competitions in a world championship?'
print '%.6f' % (1 - binomial(0, 5, 1. / 120))

"""
What is the probability of gettinger two heads when flipping a coin 5 times?
0.312500

What is the probability of getting fours ones in a rown when throwing a die?
0.000772

What is the probability that a skier will experience a ski break during five
 competitions in a world championship?
0.040978
"""
