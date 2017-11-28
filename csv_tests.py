import pandas as pd
import numpy as np
from io import StringIO

# Could we make the case for line 2 with engine='c' like all the other lines?

# Problems for both
data = "col1\n1,2,3\na,b,c"
# print(pd.read_csv(StringIO(data), index_col=[0], engine='python'))
# print(pd.read_csv(StringIO(data), index_col=[0], engine='c')) # default

data = "col1,col2\na,b,c,d,e\n1,2,3,4,5"
# print(pd.read_csv(StringIO(data), index_col=[0, 2], engine='python'))
# print(pd.read_csv(StringIO(data), index_col=[0, 2], engine='c')) # default

data = "col1,co2\na,b,c\nd,e,f\ng,h,i\n1,2,3,4,5\nj,k,l"
# print(pd.read_csv(StringIO(data), index_col=[0], engine='python'))
print(pd.read_csv(StringIO(data), index_col=[0], engine='c')) # default

data = """col1,col2\na,b,c,d\n1,2,3,4\ng,h,i,j,k"""
# print(pd.read_csv(StringIO(data), index_col=[0, 1], engine='python'))
# print(pd.read_csv(StringIO(data), index_col=[0, 1], engine='c')) # default

# Problems for C Parser Only
data = "col1\na,b\n1,2,3\nc,d" # this fails for c parser only
print(pd.read_csv(StringIO(data), index_col=[0], engine='python'))
print(pd.read_csv(StringIO(data), index_col=[0], engine='c')) # default

data = "col1\n1,2,3\na,b\nc,d" # this fails for both
print(pd.read_csv(StringIO(data), index_col=[0], engine='python'))
print(pd.read_csv(StringIO(data), index_col=[0], engine='c')) # default

data = "col1\na,b\nc,d\n1,2,3" # this fails for both
print(pd.read_csv(StringIO(data), index_col=[0], engine='python'))
print(pd.read_csv(StringIO(data), index_col=[0], engine='c')) # default
