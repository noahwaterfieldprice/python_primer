# Exercise 3.34
# Author: Noah Waterfield Price

def count_pairs(dna, pair):
    pair = tuple(pair)
    i = 0
    for p1, p2 in zip(dna[:-1], dna[1:]):
        if (p1, p2) == pair:
            i += 1
    return i

dna = 'ATATGCGGACCTAT'
pair = 'AT'
print count_pairs(dna, pair)

"""
Sample run:
python count_pairs.py
3
"""
