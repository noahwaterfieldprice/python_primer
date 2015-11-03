# Exercise 2.17
# Author: Noah Waterfield Price

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
for i in q:  # i is sub list of q
    for j in range(len(i)):  # j is integer
        print i[j],

"""
Sample run:
python nested_list_iter.py
a b c d e f g h
"""
