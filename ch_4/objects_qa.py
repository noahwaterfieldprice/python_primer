# Exercise 4.4
# Author: Noah Waterfield Price

val = eval(raw_input('Enter input value:\n'))
print '%s is a Python %s object' % (val, type(val))

"""
Sample run:
python objects_qa.py
Enter input value:
1
1 is a Python <type 'int'> object
python objects_qa.py
Enter input value:
1.0
1.0 is a Python <type 'float'> object
python objects_qa.py
Enter input value:
1 + 1j
(1 + 1j) is a Python <type 'complex'> object
python objects_qa.py
Enter input value:
[1,2]
[1,2] is a Python <type 'list'> object
python objects_qa.py
Enter input value:
(1,2)
(1,2) is a Python <type 'tuple'> object
"""
