import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(32).reshape(2,4,4)
print(a3)

# Transpose
print(np.transpose(a2))
print(a2.T)                         # shortcut

# Ravel: is a function (or method) used to flatten a multi-dimensional array into a single-dimensional (1D) array.
print(a2.ravel())
print(a3.ravel())

# flatten: same as ravel() but it always creates a physical copy of the data.
print(a3.flatten())


# Horizontal Stacking
a4 = np.arange(12,24).reshape(3,4)
print(f"a4 is {a4}")
print(np.hstack((a2,a4,a2)))

# Vertical stacking
print(np.vstack((a2,a4)))


# Horizontal split
print(np.hsplit(a4,2))

# vertical split
print(np.vsplit(a4,3))