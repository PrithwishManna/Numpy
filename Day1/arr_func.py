## Array Functions
import numpy as np

a1 = np.random.random((3,3))          # Think of it like an address: Library.Module.Function. random(...): This is the specific Function inside that sub-module that generates random floats between 0.0 and 1.0.
a1 = np.round(a1*100)
print(a1)

# max/min/sum/prod (Globally)
print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

# row and column-wise for all: 0 -> column, 1 -> row
print(np.max(a1,axis=1))
print(np.min(a1,axis=0))

# mean/median/standard divition/varience
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

# row and column-wise for all: 0 -> column, 1 -> row
print(np.std(a1,axis=1))
print(np.var(a1,axis=0))

# Trigonometric functions
print(np.sin(a1))

# Dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(10,22).reshape(4,3)
print(np.dot(a2,a3))

# log and exponents
print(np.log(a2))
print(np.exp(a3))

# round/floor/ceil : Think of it like a multi-story building: floor looks at the ground, ceil (ceiling) looks at the roof, and round looks at whichever is closer.
print(np.round(np.random.random((4,3))*100))            # 92.6 -> 93.0,  93.4 -> 93
print(np.floor(np.random.random((3,5))*100))            # 99.9 -> 99.0
print(np.ceil(np.random.random((2,3))*100))             # 10.1 -> 11.0