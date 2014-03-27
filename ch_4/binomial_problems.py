from binomial_distribution import binomial

print 'What is the probability of gettinger two heads when flipping a coin 5 times?'
print str(binomial(2, 5, 0.5)) + '\n'
print 'What is the probability of getting fours ones in a rown when throwing a die?'
print str(binomial(4, 4, 1. / 6)) + '\n'
print 'What is the probability that a skier will experience a ski break during five\n' \
    'competitions in a world championship?'
print 1 - binomial(0, 5, 1. / 120)
