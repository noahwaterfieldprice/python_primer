# Exercise 2.8
primes = [2, 3, 5, 7, 11, 13]

for prime in primes:
    print prime,

p = 17
primes.append(p)
print '\n'
for prime in primes:
    print prime,

"""
Sample run:
python primes.py
2 3 5 7 11 13 

2 3 5 7 11 13 17
"""
