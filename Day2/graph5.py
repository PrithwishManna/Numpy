# sigmoid  [Y = 1 / (1 + e^(-X))]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15,15,150)
y = 1 / (1 + np.exp(-x))

plt.plot(x,y)
plt.show()