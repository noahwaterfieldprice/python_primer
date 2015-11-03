# Exercise 7.10
# Author: Noah Waterfield Price

class Hello:

    def __call__(self, string):
        print 'Hello, ' + string + '!'

    def __str__(self):
        return 'Hello, World!'

a = Hello()
print a('students')
print a

"""
Sample run:
python Hello.py
Hello, students!
None
Hello, World!
"""
    