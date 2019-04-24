import numpy as np
import matplotlib.pyplot as plt

def sqr(t):
    return t**2
def cube(t):
    return t**3
def quad(t):
    return t**4

t1 = np.arange(0,100)
plt.figure(1)

plt.subplot(311)
plt.grid()
plt.plot(t1,sqr(t1), 'b-')

plt.subplot(312)
plt.grid()
plt.plot(t1,cube(t1), 'g^')

plt.subplot(313)
plt.plot(t1, quad(t1), 'y.')


plt.figure(2)

plt.subplot(221)
plt.grid()
plt.plot(t1,sqr(t1), 'b-')

plt.subplot(224)
plt.grid()
plt.plot(t1,cube(t1), 'g^')

plt.show()
