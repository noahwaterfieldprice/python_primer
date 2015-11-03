# Exercise 3.35
# Author: Noah Waterfield Price

def count_substr(dna, substr):
    i = 0
    for p in xrange(len(dna)):
        if dna[p] == substr[0]:
            if dna[p:p + len(substr)] == substr:
                i += 1
    return i

dna = 'ATATGCGGATACCTATA'
substr = 'ATA'
print count_substr(dna, substr)

"""
Sample run:
python count_substr.py
3
"""
