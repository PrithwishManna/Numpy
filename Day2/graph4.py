# y = xlog x

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,15,150)
y = x * np.log(x)

plt.plot(x, y)
plt.show()