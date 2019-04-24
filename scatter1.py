import matplotlib.pyplot as plt
from pylab import randn

x=randn(200)
y=randn(200)
plt.figure(1)
one=plt.scatter(x,y,color='r')

plt.figure(2)
two=plt.scatter(x,y,s=10, facecolor='none', edgecolor='b')
plt.show()
