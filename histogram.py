import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')
iris_setosa=iris.loc[iris['species']=='setosa']
iris_verginica=iris.loc[iris['species']=='virginica']
iris_versicolor=iris.loc[iris['species']=='versicolor']

plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_setosa['petal_length']), 'o')
plt.plot(iris_verginica['petal_length'], np.zeros_like(iris_verginica['petal_length']),'o')
plt.plot(iris_versicolor['petal_length'],np.zeros_like(iris_versicolor['petal_length']),'o')

#plt.show()

sb.FacetGrid(iris, hue='species', height=5)\
                   .map(sb.distplot, 'petal_length')\
                   .add_legend();

sb.FacetGrid(iris, hue='species', height=5)\
                   .map(sb.distplot, 'petal_width')\
                   .add_legend();

sb.FacetGrid(iris, hue='species', height=5)\
                   .map(sb.distplot, 'sepal_length')\
                   .add_legend();

sb.FacetGrid(iris, hue='species', height=5)\
                   .map(sb.distplot, 'sepal_width')\
                   .add_legend();
plt.show();
