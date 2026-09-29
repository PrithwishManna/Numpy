## array attributes
import numpy as np

a1 = np.arange(10)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)                        ## first(2) denotes the no. of 2D array and last two are rows and columns 

# ndim  -> It gives output 'number of dimension'
print(a3.ndim)

# shape  -> It gives output 'no. of rows and columns'
print(a2.shape)

# size   -> It gives the total no. of elements
print(a2.size)

# itemsize
print(a2.itemsize)

# dtype                             
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

## Changing Datatypes
# astype
print(a3.astype(np.int32))
