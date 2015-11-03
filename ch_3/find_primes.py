# Exercise 3.33
# Author: Noah Waterfield Price

def Sieve_of_Eratosthenes(N):
    numbers = range(2, N + 1)
    primes = []
    for p in xrange(len(numbers)):
        if numbers[p] != 0:
            primes.append(numbers[p])
            for i in xrange(numbers[p], N + 1, numbers[p]):
                numbers[i - 2] = 0
    return primes

primes100 = Sieve_of_Eratosthenes(100)
print primes100

"""
Sample run:
python find_primes.py
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
