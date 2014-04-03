# Exercise 6.21
from numpy import *
from scitools.StringFunction import StringFunction


def convert2strfunc(specification):
    func, varpar = specification.split(' is a function of ')
    strfunc = "StringFunction('%s', " % func
    if varpar.find('parameter') != -1:
        var, par = varpar.split(' with parameter ')
        var = [v.strip() for v in var.split(',')]
        par = [p.strip() for p in par.split(',')]
        strfunc += "independent_variables=('%s'), %s)" % \
            ("', '".join(var), ', '.join(par))
    else:
        var = [v.strip() for v in varpar.split(',')]
        strfunc += "independent_variables=('%s'))" % \
            ("', '".join(var))
    print strfunc   # print what is passed to eval
    return eval(strfunc)


infile = open('function_specifications.txt', 'r')
for specification in infile:
    convert2strfunc(specification)
infile.close()

"""
Sample run:
python Exercise 6.21
StringFunction('sin(x)', independent_variables=('x'))
StringFunction('sin(a*y)', independent_variables=('y'), a=2)
StringFunction('sin(a*x-phi)', independent_variables=('x'), a=3, phi=-pi)
StringFunction('exp(-a*x)*cos(w*t)', independent_variables=('t'), a=1, w=pi, x=2)
StringFunction('b*ln(x)*tan(y/a)', independent_variables=('x', 'y'), a=3, b=0.5)
StringFunction('2*cos(p*x)*sin(q*y)', independent_variables=('x', 'y'), p=10, q=17)
StringFunction('sin(a*pi*x/8)*(2*pi)**-0.5*1/s*exp(-0.5*((t-m)/s)**2)', independent_variables=('x', 't'), a=0.5, s=10, m=0.2)
"""
