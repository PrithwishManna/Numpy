import numpy as np

a = np.random.randint(1,100,25)
b = np.random.randint(1,100,24).reshape(6,4)

# np.flip   (mirror image)
print(np.flip(a))                           # mirror image of the array
print(np.flip(b))                           # first mirror image of column-wise and then row-wise**
print(np.flip(b,axis=0))                    # column-wise
print(np.flip(b,axis=1))                    # row-wise

# np.put.   (Do permanent change)
np.put(a,[0,1],[21,4])
print(a)

# np.delete
print(np.delete(a,0))       # this is temporery

# set functions
m = np.array([1,2,4,3,6])
n = np.array([2,5,3,4,7])

print(np.union1d(m,n))
print(np.intersect1d(m,n))
print(np.setdiff1d(m,n))
print(np.setxor1d(m,n))
print(np.isin(m,1))
print(m[np.isin(m,[1,3,7])])

# np.clip
print(np.clip(a,a_min=25,a_max=75))             # any element which is smaller, bigger than 25, 75 that is replaced by 25, 75 respectively


