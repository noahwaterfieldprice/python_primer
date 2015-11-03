# Exercise 6.24
# Author: Noah Waterfield Price

from numpy import zeros
objects = [
    '""',            # empty string
    '"string"',     # non-empty string
    '[]',           # empty list
    '[0]',          # list with one element
    '()',           # empty tuple
    '(0,)',          # tuple with one element
    '{}',           # empty dict
    '{0:0}',        # dict with one element
    '0',            # int zero
    '0.0',          # float zero
    '0j',           # complex zero
    '10',           # int 10
    '10.',          # float 10
    '10j',          # imaginary 10
    'zeros(0)',     # empty array
    'zeros(1)',     # array with one element (zero)
    'zeros(1)+10',  # array with one element (10)
    'zeros(2)',     # array with two elements (watch out!)
]
for element in objects:
    object = eval(element)
    print 'object = %s; if object is %s' % \
        (element, bool(object))

"""
Sample run:
python boolean_context.py
object = ""; if object is False
object = "string"; if object is True
object = []; if object is False
object = [0]; if object is True
object = (); if object is False
object = (0,); if object is True
object = {}; if object is False
object = {0:0}; if object is True
object = 0; if object is False
object = 0.0; if object is False
object = 0j; if object is False
object = 10; if object is True
object = 10.; if object is True
object = 10j; if object is True
object = zeros(0); if object is False
object = zeros(1); if object is False
object = zeros(1)+10; if object is True
Traceback (most recent call last):
  File "/Users/Noah/dev/apospwp/ch_6/boolean_context.py", line 26, in <module>
    (element, bool(object))
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
"""
