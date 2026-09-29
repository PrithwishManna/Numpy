## fancy indexing
import numpy as np

a = np.arange(24).reshape(6,4)
print(a)
# print 1st, 3rd, 4th and last row
print(a[[0,2,3,5]])
# print 1st, 3rd and last column
print(a[:,[0,2,3]])

## Boolean indexing
a = np.random.randint(1,100,24).reshape(6,4)
print(a)
# Find all numbers greater than 50
print(a > 50)
print(a[a > 50])
print(a[a % 2 == 0])                                    # find out even numbers
# Find all numbers greater than 50 and are even
print(a[(a > 50) & (a % 2 == 0)])
print(a[a % 7 != 0])          # a[~(a % 7 == 0)]        # find all numbers which is not divisible by 7

