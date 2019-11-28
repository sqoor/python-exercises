import numpy as np
import pandas as pd

# 1
print('# 1 ---------------------------------------')
data = [2, 3, 6, 8, 10]
arr = pd.Series(data)
print(arr)

# 2
print('\n\n# 2 ---------------------------------------')
data = {
    'a': [100],
    'b': [200],
    'c': [300],
    'd': [400],
    'e': [800]
}

d = pd.DataFrame(data)
print(d)

# 3
print('\n\n# 3 ---------------------------------------')
data = [20, 10, 150, 110, 100, 50]
d = pd.Series(data)
d.plot('pie')

# 4
print('\n\n# 4 ---------------------------------------')
data = {
    'd1': [100, 200, 5, 400, 700, 100, 200, 50, 400, 700],
    'd2': [140, 0, 300, 400, 200, 140, 0, 700, 400, 200]
}

d = pd.DataFrame(data)

d.plot()

# 5
print('\n\n# 5 ---------------------------------------')
data = {
    'x': [78, 85, 96, 80, 86],
    'y': [84, 94, 89, 83, 86],
    'z': [86, 87, 86, 72, 83]
}

d = pd.DataFrame(data)
print(d)

# 6
# print('\n\n# 6 ---------------------------------------')
df = {
    'name': ["Bob", "Jessica", 'Mary', "John", "Mel"],
    'births': [986, 155, 77, 578, 973]
}

df = pd.DataFrame(df)
plot = df.plot.pie(y='births', figsize=(5, 5))

# 7
print('\n\n# 7 ---------------------------------------')

df = pd.read_csv('myDataFrame.csv', sep='\t', index_col=0)
print(df)
df.describe()

df.to_csv('df2.csv', sep=',', encoding='utf-8')


# 8
print('\n\n# 8 ---------------------------------------')
dates = pd.date_range('20000101', periods=4)
df = pd.DataFrame(np.random.randn(4, 2), index=dates, columns=list('AB'))

print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104', ['A']])
print(df.iloc[:1:2])
print(df[df > 0])
print(df[df.B > 0])
df['A'] = [100, 200, 300, 100]
print(df)
print(df[df['A'].isin([200, 300])])
