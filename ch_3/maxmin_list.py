# Exercise 3.23
# Author: Noah Waterfield Price

def mymax(a):
    max_elem = a[0]
    for elem in a:
        if elem > max_elem:
            max_elem = elem
    return max_elem


def mymin(a):
    min_elem = a[0]
    for elem in a:
        if elem < min_elem:
            min_elem = elem
    return min_elem

print mymax([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5])
print mymin([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5])

"""
Sample run:
python maxmin_list.py
11
-7
"""
