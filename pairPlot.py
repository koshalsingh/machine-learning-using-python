import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris=pd.read_csv('iris.csv')
plt.close()
sb.set_style('whitegrid')
sb.pairplot(iris,hue='species', height=5)
plt.show()
