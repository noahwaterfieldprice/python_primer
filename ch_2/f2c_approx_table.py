# Exercise 2.2
# Author: Noah Waterfield Price

print '------------------------'     					# table heading
F = 0                        					# start value for F
dC = 10                         				# increment of F in loop
print '%6s %8s %8s' % ('F', 'C', '~C')  # column headers
while F <= 100:
    C = (5. / 9) * (F - 32)
    C_approx = 0.5 * (F - 30)
    print '%6.2f %8.2f %8.2f' % (F, C, C_approx)
    F = F + dC
print '------------------------'     			# end of table line (after loop)

"""
Sample run:
python f2c_approx_table.py
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
