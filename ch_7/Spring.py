# Exercise 7.7
class Spring:

    def __init__(self, k):
        self.k = k

    def force(self, x):
        return self.k * x

    def energy(self, x):
        return 0.5 * self.k * x ** 2


def table(f, a, b, n, heading=''):
    """Write out f(x) for x in [a,b] with steps h=(b-a)/n."""
    print '-'*42
    print heading
    print '-'*42
    h = (b-a)/float(n)
    for i in range(n+1):
        x = a + i*h
        print 'function value = %10.4f at x= %g' % (f(x), x)
    print '-'*42 + '\n'
spring = Spring(3)

table(spring.force, 0, 10, 11, 'Spring force table')
table(spring.energy, 0, 10, 11, 'Spring energy table')

"""
Sample run:
python Spring.py
------------------------------------------
Spring force table
------------------------------------------
function value =     0.0000 at x= 0
function value =     2.7273 at x= 0.909091
function value =     5.4545 at x= 1.81818
function value =     8.1818 at x= 2.72727
function value =    10.9091 at x= 3.63636
function value =    13.6364 at x= 4.54545
function value =    16.3636 at x= 5.45455
function value =    19.0909 at x= 6.36364
function value =    21.8182 at x= 7.27273
function value =    24.5455 at x= 8.18182
function value =    27.2727 at x= 9.09091
function value =    30.0000 at x= 10
------------------------------------------

------------------------------------------
Spring energy table
------------------------------------------
function value =     0.0000 at x= 0
function value =     1.2397 at x= 0.909091
function value =     4.9587 at x= 1.81818
function value =    11.1570 at x= 2.72727
function value =    19.8347 at x= 3.63636
function value =    30.9917 at x= 4.54545
function value =    44.6281 at x= 5.45455
function value =    60.7438 at x= 6.36364
function value =    79.3388 at x= 7.27273
function value =   100.4132 at x= 8.18182
function value =   123.9669 at x= 9.09091
function value =   150.0000 at x= 10
------------------------------------------

"""
