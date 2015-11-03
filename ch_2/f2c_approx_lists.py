# Exercise 2.18
# Author: Noah Waterfield Price

F = [i for i in range(0, 110, 10)]
C = [(5. / 9) * (F[i] - 32) for i in range(len(F))]
C_approx = [0.5 * (F[i] - 30) for i in range(len(F))]

conversion = [[Fval, Cval, C_approxval]
              for Fval, Cval, C_approxval in zip(F, C, C_approx)]

print '------------------------'
print '%6s %8s %8s' % ('F', 'C', '~C')  # column headers
for Fval, Cval, C_approxval in conversion:
    print '%6.2f %8.2f %8.2f' % (Fval, Cval, C_approxval)
print '------------------------'

"""
Sample run:
python f2c_approx_lists.py
------------------------
     F        C       ~C
  0.00   -17.78   -15.00
 10.00   -12.22   -10.00
 20.00    -6.67    -5.00
 30.00    -1.11     0.00
 40.00     4.44     5.00
 50.00    10.00    10.00
 60.00    15.56    15.00
 70.00    21.11    20.00
 80.00    26.67    25.00
 90.00    32.22    30.00
100.00    37.78    35.00
------------------------
"""
