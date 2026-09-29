## creating np arrays

import numpy as np
p = np.array([1,2,3])
print(p)
print(type(p))

# 2D, 3D arrays
q = np.array([[1,2,3],[3,4,3]])
print(q)
r = np.array([[[1,2,5],[2,8,0]],[[3,9,1],[2,5,1]]])                 ## Tensor
print(r)

# dtype
x = np.array([2,7,3],dtype = float)
print(x)
y = np.array([2,0,3],dtype = bool)
print(y)
z = np.array([2,7,3],dtype = complex)
print(z)

# np.arange
a = np.arange(1,13)
print(a)
b = np.arange(1,11,2)                   # slicing
print(b)

# reshape
c = a.reshape(4,3)                      # 2 x 5 matrix
print(c)
d = a.reshape(2,6)                      # 3 x 4 matrix
print(d)
f = np.arange(16).reshape(2,2,2,2)
print(f)

# np.ones and np.zeros
g = np.ones((2,3))                      # it creates a (2 x 3) matrix with elements 1.0(in float) 
print(g)
h = np.zeros((2,3))                     # it creates a (2 x 3) matrix with elements 0.0(in float) 
print(h)

# np.random
k = np.random.random((3,4))             # it creates a (3 x 4) matrix with random elements between (0 to 1)
print(k)

# np.linspace
l = np.linspace(-10, 10,5)              # [start, stop, number of points in [start,stop]]
print(l)

# np.identity
I = np.identity(3)                      # creats (3 x 3) identity matrix
print(I)