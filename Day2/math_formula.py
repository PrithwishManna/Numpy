import numpy as np

a = np.arange(10)
print(np.sum(a))
print(np.sin(a))
## sigmoid function
def sigmoid(arr):
    return 1/(1 + np.exp(-(arr)))

print(sigmoid(10))
## Mean squared error
p = np.random.randint(1,50,25)
q = np.random.randint(1,50,25)

def mse(arr1,arr2):
    return np.mean((arr1 - arr2) ** 2)
print(mse(p,q))

## Binary Cross Entropy / Log Loss for Binary Classification
