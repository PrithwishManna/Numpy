# y = sin x

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15,15,150)
y = np.sin(x)

plt.plot(x, y)
plt.show()