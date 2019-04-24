import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('populations.txt')
year, hare, lynex, carrot=data.T
print(year)
print(hare)
print(lynex)
print(carrot)

population = data[:,1:]
#print(population)
lines=plt.plot(year,hare, year,  lynex, year, carrot)
plt.setp(lines[0], color='r', label='hare')
plt.setp(lines[1], color='g', label='lynex')
plt.setp(lines[2], color='b', label='carrot')
plt.legend()
plt.show()
