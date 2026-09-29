### array operators
## scalar operations
import numpy as np
a1 = np.arange(12,dtype=float).reshape(3,4)
a2 = np.arange(1, 13).reshape(3,4)
print(a1)

# arithmetic    (+\-\*\/\**)
print(a1 + 2)
print(a1 - 4)
print(a1 * 3)
print(a1 / 2)
print(a1 ** 3)

# relational     (>\>=\<\<=\==\!=)
print(a1 > 5)
print(a1 == 6)


## vector operations
print(a1 + a2)
print(a1 * a2)
print(a1 / a2)
print(a1 ** a2)
print(a1 - a2)