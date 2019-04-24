import pandas as pd

df= pd.read_csv('nyc_weather.csv')
#print(df)
print(df['Temperature'].max())
df['EST'],[df['Events']=='Rain']

print(df.EST[df['Events']=='Rain'])
print(df[df.Events=='Rain'])
