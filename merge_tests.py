import pandas as pd

df1 = pd.DataFrame({'id':[1.,2.], 'c1':[10,20]})

df2 = pd.DataFrame({'id':[2], 'c2':[200]})

df = df1.merge(df2, on='id', how='left')

print(df)
print(df['id'].dtype)
