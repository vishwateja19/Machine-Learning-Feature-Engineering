a=1

print(a)

import pandas as pd 
df = pd.read_csv('titanic.csv')

df.isnull().sum()

df['Age'].hist(bins = 50)

df['Age'].plot(kind = 'kde',)