# working with missing values -> np.nan

import numpy as np

a = np.array([2,3,.9,.34,-2,np.nan,10])
print(a)
#print(np.isnan(a))                      # find nan value
#print(a[np.isnan(a)])                   # print nan value in a
print(a[~np.isnan(a)])                   # print except the nan value

