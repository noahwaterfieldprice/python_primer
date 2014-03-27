def diff(f, x, h=1E-6):
	return 1/(2*h)*(f(x+h) - f(x-h))

from math import exp, cos, sin, pi, log

f1 = lambda x: exp(x)
df1 = lambda x: exp(x)
f2 = lambda x: exp(-2*x**2)
df2 = lambda x: -4*x*exp(-2*x**2)
f3 = lambda x: cos(x)
df3 = lambda x: -sin(x)
f4 = lambda x: log(x)
df4 = lambda x: 1/x

funcs = [f1, f2, f3, f4]
diff_funcs = [df1, df2, df3 ,df4]
func_names = ['exp(x)', 'exp(-2x^2)', 'cos(x)', 'ln(x)']
values = [0, 0, 2*pi, 1]

print '%10s %8s %8s %8s' % ('function', 'exact', 'approx', 'values') 

for name, f, df, x in zip(func_names, funcs, diff_funcs, values):
	exact = df(x)
	approx = diff(f, x, h=0.01)
	error = abs(exact - approx)
	print '%10s %.6f %.6f %.6f' % (name, exact, approx, error) 

"""
Sample run:
python diff_f.py
  function    exact   approx   values
    exp(x) 1.000000 1.000017 0.000017
exp(-2x^2) 0.000000 0.000000 0.000000
    cos(x) 0.000000 0.000000 0.000000
     ln(x) 1.000000 1.000033 0.000033
"""
	