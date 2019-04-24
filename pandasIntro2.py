import pandas as pd

df = pd.read_csv('weather_data.csv')
print(df)

weather_data=[('1/1/2017', 32, 6, 'Rain'),
                ('1/2/2017', 35, 7, 'Sunny'),
                ('1/3/2017', 28, 2, 'Snow'),
                ('1/4/2017', 24, 7, 'Snow'),
                ('1/5/2017', 32, 4, 'Rain'),
                ('1/6/2017', 31, 2, 'Sunny')
               ]
df1=pd.DataFrame(weather_data,columns=['day','temperature', 'windSpeed','event'])
print(df1)
print(df.shape)#total number of rows and columns
print(df1.shape)

#if you want to see initial some rows then use head command (default 5 rows)
print(df.head())

#if you want to see last few rows then use tail command (default last 5 rows will print)
print(df.tail())

#slicing
print(df[2:5])

#print columns in a table
print(df.columns)

#print particular column data
print(df.day)
print(df['day'])
print(df[['day', 'temperature']])

#print max temperature
print(df['temperature'].max())

print(df['temperature'].describe())

# select rows which has maximum temperature
print(df[df.temperature==df.temperature.max()])

#select only day column which has maximum temperature
df.day[df.temperature == df.temperature.max()] 
