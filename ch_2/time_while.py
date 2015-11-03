# Exercise 2.25
# Author: Noah Waterfield Price

import time

t0 = time.time()
while time.time() - t0 < 10:
    print '....I like while loops!'
    # time.sleep(2)
print 'Oh, no - the loop is over.'

t0 = time.time()
while time.time() - t0 > 10:
    print '....I like while loops!'
    time.sleep(2)
print 'Oh, no - the loop is over.'

"""
Sample run:
python time_while.py
....I like while loops!
....I like while loops!
....I like while loops!
....I like while loops!
....I like while loops!
Oh, no - the loop is over.
Oh, no - the loop is over.
"""
