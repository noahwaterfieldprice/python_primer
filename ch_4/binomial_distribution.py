# Exercise 4.24
# Author: Noah Waterfield Price

import sys


def fact(n):
    ans = 1
    if n == 0 or n == 1:
        return ans
    else:
        while n > 0:
            ans *= n
            n -= 1
    return ans


def binomial(x, n, p):
    B = float(fact(n)) / (fact(x) * fact(n - x)) * p ** x * (1 - p) ** (n - x)
    return B

if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
        n = int(sys.argv[2])
        p = float(sys.argv[3])
    except IndexError:
        print 'x, n and p must be supplied on the command line'
        sys.exit(1)
    except ValueError:
        print 'x and n must be real integers'
        sys.exit(1)

    print binomial(x, n, p)

"""
Sample run:
python binomial_distribution.py 3 3 0.5
0.125
python binomial_distribution.py 2 5 0.5
0.3125
"""
