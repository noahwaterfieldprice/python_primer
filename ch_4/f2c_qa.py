# Exercise 4.1
# Author: Noah Waterfield Price

F = raw_input("Enter a temperature in Fahrenheit:\n")
F = float(F)
C = 5 / 9. * (F - 32)
print "%g Fahrenheit = %g Celsius" % (F, C)

"""
Sample run:
python f2c_qa.py
Enter a temperature in Fahrenheit:
243
243 Fahrenheit = 117.222 Celsius
"""
