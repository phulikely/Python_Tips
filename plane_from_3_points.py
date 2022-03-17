import numpy as np

p1 = np.array([-3.16, 0.52, 3.88])
p2 = np.array([-0.78, 0.56, 3.88])
p3 = np.array([2.23, 0.58, 3.88])

# These two vectors are in the plane
v1 = p3 - p1
v2 = p2 - p1

# the cross product is a vector normal to the plane
cp = np.cross(v1, v2)
a, b, c = cp

# This evaluates a * x3 + b * y3 + c * z3 which equals d
d = np.dot(cp, p3)

print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))
