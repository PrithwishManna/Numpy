# y = x^2

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-15,15,150)
y = x ** 2

plt.plot(x, y)
plt.show()