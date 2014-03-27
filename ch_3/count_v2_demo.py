def count_v2_demo(dna, base):
    print 'dna:', dna
    print 'base:', base
    i = 0  # counter
    for c in dna:
        print 'c:', c
        if c == base:
            print 'True if test'
            i += 1
    return i

n = count_v2_demo('ATGCGGACCTAT', 'C')
print n

"""
Sample run:
python count_v2_demo.py
dna: ATGCGGACCTAT
base: C
c: A
c: T
c: G
c: C
True if test
c: G
c: G
c: A
c: C
True if test
c: C
True if test
c: T
c: A
c: T
3
"""
