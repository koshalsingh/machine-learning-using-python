import pandas as pd

df = pd.read_csv('weather_data_cities.csv')
print(df)
g=df.groupby('city')
print(g)
for cit, cit_df in g:
        print(cit)
        print(cit_df)
print(g.max())
