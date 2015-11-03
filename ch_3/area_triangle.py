# Exercise 3.9
# Author: Noah Waterfield Price

def area(vert):
    A = 0.5 * abs(vert[1][0] * vert[2][1] - vert[2][0] * vert[1][1] -
                  vert[0][0] * vert[2][1] + vert[2][0] * vert[0][1] +
                  vert[0][0] * vert[1][1] - vert[1][0] * vert[0][1])
    return A

v1 = (0, 0)
v2 = (1, 0)
v3 = (0, 2)
vertices = [v1, v2, v3]
triangle1 = area(vertices)

print 'Area of triangle is %.2f' % triangle1

"""
Sample run:
python area_triangle.py
Area of triangle is 1.00
"""
