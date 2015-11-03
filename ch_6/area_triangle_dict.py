# Exercise 6.15
# Author: Noah Waterfield Price

def area(vert):
    A = 0.5 * abs(vert[2][0] * vert[3][1] - vert[3][0] * vert[2][1] -
                  vert[1][0] * vert[3][1] + vert[3][0] * vert[1][1] +
                  vert[1][0] * vert[2][1] - vert[2][0] * vert[1][1])
    return A

v1 = (0, 0)
v2 = (1, 0)
v3 = (0, 2)
vertices = {1: v1, 2: v2, 3: v3}
triangle1 = area(vertices)

print 'Area of triangle is %.2f' % triangle1

"""
Sample run:
python area_triangle_dict.py
Area of triangle is 1.00
"""