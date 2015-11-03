# Exercise 6.16
# Author: Noah Waterfield Price

def poly1(data, x):  # Evaluate polynomial given as dict
    return sum([data[p] * x ** p for p in data])


def poly2(data, x):  # Evaluate polynomial given as list
    return sum([data[p] * x ** p for p in range(len(data))])

poly_dict = {0: -0.5, 100: 2}
print poly_dict

poly_list = [0]*101
poly_list[0] = -0.5
poly_list[100] = 2
print poly_list


import time
t0 = time.clock()
[poly1(poly_dict, 1.05) for p in range(200)]
t1 = time.clock()
[poly2(poly_list, 1.05) for p in range(200)]
t2 = time.clock()

f = (t1 - t0) / (t2 - t1)
print 'Time taken: poly1 (dictionary) / poly2 (list) =', f

"""
Sample run:
python poly_repr.py
{0: -0.5, 100: 2}
[-0.5, 0, 0, ... 0, 0, 0, 2]
Time taken: poly1 (dictionary) / poly2 (list) = 0.0503753935578
"""
