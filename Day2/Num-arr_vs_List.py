# speed
## list

a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]
c = []
import time

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time() - start)


## Numpy
import numpy as np
p = np.arange(10000000)
q = np.arange(10000000,20000000)

sat = time.time()
c = a + b
print(time.time() - sat)