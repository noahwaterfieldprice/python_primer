# Exercise 7.13
# Author: Noah Waterfield Price

class Central:

    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - f(x - h)) / (2 * h)


if __name__ == '__main__':
    def f(x):
        return 0.25 * x ** 4

    df = Central(f)
    for x in (1, 5, 10):
        df_value = df(x)
        exact = x ** 3
        print "f'(%d)=%g (error=%.2E)" % (x, df_value, exact - df_value)

    from math import log

    print '-' * 45
    print '%-13s %8s %8s %8s' % ('', 'x=0.1', 'x=3', 'x=20')
    print '-' * 45
    for h in (0.5, 0.1, 1E-3, 1E-5, 1E-7, 1E-9):
        df = Central(log, h)
        print 'h = %-7.0E |' % h
        print '%-11s | %9.2E %9.2E %9.2E' % ("f' (exact)",
                                             1 / 1.1,
                                             1 / 3.,
                                             1 / 20.)
        print '%-11s | %9.2E %9.2E %9.2E' % ("f' (approx)",
                                             df(1.1),
                                             df(3),
                                             df(20))
        print '%-11s | %9.2E %9.2E %9.2E' % ("error",
                                             1 / 1.1 - df(1.1),
                                             1 / 3. - df(3),
                                             1 / 20. - df(20))

        print '-' * 45

"""
Sample run:
python Central.py
f'(1)=1 (error=-1.01E-10)
f'(5)=125 (error=4.38E-09)
f'(10)=1000 (error=4.64E-08)
---------------------------------------------
                 x=0.1      x=3     x=20
---------------------------------------------
h = 5E-01   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.81E-01  3.36E-01  5.00E-02
error       | -7.17E-02 -3.14E-03 -1.04E-05
---------------------------------------------
h = 1E-01   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.12E-01  3.33E-01  5.00E-02
error       | -2.52E-03 -1.24E-04 -4.17E-07
---------------------------------------------
h = 1E-03   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.09E-01  3.33E-01  5.00E-02
error       | -2.50E-07 -1.23E-08 -4.18E-11
---------------------------------------------
h = 1E-05   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.09E-01  3.33E-01  5.00E-02
error       | -3.13E-11 -2.18E-12 -6.99E-12
---------------------------------------------
h = 1E-07   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.09E-01  3.33E-01  5.00E-02
error       | -5.43E-10  1.29E-09  3.04E-10
---------------------------------------------
h = 1E-09   |
f' (exact)  |  9.09E-01  3.33E-01  5.00E-02
f' (approx) |  9.09E-01  3.33E-01  5.00E-02
error       | -7.40E-08 -2.76E-08 -4.14E-09
---------------------------------------------
"""
