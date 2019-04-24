import numpy as np
import matplotlib.pyplot as plt

a=np.arange(0,5,0.2)
plt.plot(a, a**2, 'gs', label='^2')
plt.plot(a, a**2.2, 'r^', label='^2.2')
plt.plot(a,a**2.4, 'b--', label='^2.4')
plt.legend()
plt.grid()
plt.show()
