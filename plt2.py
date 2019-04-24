import matplotlib.pyplot as plt

x1=[10,20,30]
y1=[20,40,10]
y2=[40,10,30]
line1 = plt.plot(x1,y1, 'b', linewidth='3.0', linestyle='dashed')
line2 = plt.plot(x1,y2, 'r', linewidth='5.0', linestyle='dotted')
plt.show()
