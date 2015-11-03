# Exercise 3.19
# Author: Noah Waterfield Price

def fact(n):
    ans = 1
    if n == 0 or n == 1:
        return ans
    else:
        while n > 0:
            ans *= n
            n -= 1
    return ans

print fact(5)

"""
Sample run:
python fact.py
120
"""
