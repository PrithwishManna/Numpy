# np.sort
import numpy as np
a = np.random.randint(1,100,25)
b = np.random.randint(1,100,24).reshape(6,4)

print(np.sort(a))
print(np.sort(a)[::-1])                             # reverse sort
print(np.sort(b))                                   # sort row-wise (same as)-> np.sort(b,axis=1)
print(np.sort(b,axis = 0))                          # sort column-wise

# np.append
print(np.append(a,121))
print(np.append(b,np.ones((b.shape[0],1)),axis=1))  # b.shape[0]: This retrieves the number of rows in your matrix b (which is 6 in your case).(6, 1): This tells NumPy to create a 2D array with 6 rows and 1 column.A vertical vector of six 1.0 values.

# np.concatenate
c = np.random.randint(101,160,24).reshape(6,4)
print(np.concatenate((b,c),axis=0))                 # add vertically
print(np.concatenate((b,c),axis=1))                 # add horizontally

# np.unique
d = np.array([1,1,1,1,2,2,2,5,2,6,1,1,4,5,3,3,3,6])
print(np.unique(d))

# np.expand_dims
print(np.expand_dims(a,axis = 0))                   # this becomes (1,25)
print(np.expand_dims(a,axis = 1))                   # this becomes (25,1)

# np.where                                          # find the indices
print(np.where(a > 50))                             # find all indices with value greater than 50
print(np.where(a % 2 == 0,0,a))                     # replace all even values with 0.  -> where(condition,True,False)

# np.argmax                                         # print indices of the max element in a particular axis
print(np.argmax(a))
print(b)
print(np.argmax(b,axis = 0))            # vertically -> 0
print(np.argmax(b,axis = 1))            # horizontally -> 1

print(np.argmin(a))

# np.cumsum                             # cumulative sum
print(np.cumsum(a))
print(np.cumsum(b,axis=0))

print(np.cumprod(a))

# np.percentile
print(np.percentile(a,50))              # meaning -> half before and half after

# np.histogram                          # counts frequency
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,90,100]))
print(np.histogram(a,bins=[0,50,100]))

# np.corrcoef
salary = np.array([20000,30000,22000,50000,34000])
experience = np.array([1,3,2,5,4])

print(np.corrcoef(salary,experience))

# np.isin                                           # find multiple items at a time
items = [10,20,25,40,50,55,70,80,90]
print(a[np.isin(a,items)])
