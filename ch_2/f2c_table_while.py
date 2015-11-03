# Exercise 2.1
# Author: Noah Waterfield Price

print '------------------'     		# table heading
F = 0                        		# start value for F
dC = 10                         	# increment of F in loop
print '%6s %8s' % ('F', 'C')		# column headers
while F <= 100:                 	# loop heading with condition
    C = (5. / 9) * (F - 32)         	# 1st statement inside loop
    print '%6.2f %8.2f' % (F, C)  	# 2nd statement inside loop
    F = F + dC                 		# 3rd statement inside loop
print '------------------'     		# end of table line (after loop)

"""
Sample run:
python f2c_table_while.py
------------------
     F        C
  0.00   -17.78
 10.00   -12.22
 20.00    -6.67
 30.00    -1.11
 40.00     4.44
 50.00    10.00
 60.00    15.56
 70.00    21.11
 80.00    26.67
 90.00    32.22
100.00    37.78
------------------
"""
