import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')
print(iris.shape)
print(iris.columns)
print(iris["species"].value_counts())
iris.plot(kind='scatter', x='sepal_length', y='sepal_width')
plt.show()
sb.set_style('whitegrid')
sb.FacetGrid(iris,hue='species',height=4).map(plt.scatter,'sepal_length','sepal_width').add_legend()
plt.show()
