# Exercise 3.31
def L3(x, n=None, epsilon=None, return_n=False):
    if (n is None and epsilon is None) or \
            (n is not None and epsilon is not None):
        print 'Error: Either n or epsilon must be given (not both)'
    term = x / (1. + x)
    s = term
    if n is not None:
        for i in range(2, n + 1):
            # recursive relation between ci and c(i-1)
            term *= (i - 1.) / i * x / (1. + x)
            s += term
        return (s, n) if return_n is True else s
    elif epsilon is not None:
        i = 1
        while abs(term) > epsilon:
            i += 1
            # recursive relation between ci and c(i-1)
            term *= (i - 1.) / i * x / (1. + x)
            s += term
        return (s, i) if return_n is True else s

print L3(10, n=100)
print L3(10, n=1000, return_n=True)
print L3(10, epsilon=1e-10)
print L3(10, epsilon=1e-10, return_n=True)

"""
Sample run:
python L3_flexible.py
2.39788868474
(2.397895272798365, 1000)
2.39789527188
(2.397895271877886, 187
"""
