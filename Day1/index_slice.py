# Indexing and Slicing

import numpy as np
                                                    #[[0 1 2 3]
a1 = np.arange(10)                                  # [4 5 6 7]
a2 = np.arange(12).reshape(3,4)                     # [8 9 10 11]]
a3 = np.arange(16).reshape(2,2,2,2)                 
print(a1)
print(a2)
print(a3)

# Indexing
print(a1[-1])
print(a2[1,2])
print(a2[2,3])
print(a3[1,0,1])
print(a3[0,1,0,1])

# Slicing                                           # array[row_slice, column_slice] -> start:stop:step
print(a1[3:6])                  # [3 4 5]
print(a2[0,:])                  # [0 1 2 3]
print(a2[:,2])                  # [2 6 10]
print(a2[1:3,1:3])
print(a2[::2,::3])              
print(a2[::2,1::2])
print(a2[:2,1:])

a4 = np.arange(27).reshape(3,3,3)
print(a4)
print(a4[1])
print(a4[0,1,:])
print(a4[1,:,1])
print(a4[2,1:,1:])
print(a4[::2,0,::2])

# Iterating
for i in a1:
    print(i)
for i in a2:
    print(i)
for i in a3:
    print(i)

for i in np.nditer(a3):             # it individually print all elements
    print(i)