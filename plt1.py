import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv', parse_dates=True, index_col=0)
plt.figure(1)
print(df)
df.plot()
plt.show()
