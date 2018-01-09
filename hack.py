import pandas as pd

a = pd.DataFrame({'A': range(5),
                  'B': range(5),
                  'C': range(5)})

b = pd.DataFrame({'A': range(5),
                  'B': range(5),
                  'C': range(5)},
                  index=pd.date_range("2012-01-01", periods=5))

# # getitem with integer with loc
# print(a.loc[0, 1]) # fails because 1 is not column label
# print(b.loc[0, 1]) # fails because 0 is not row label
# print(a.loc[0, 0:2]) # slice fails because 0:2 aren't column labels
# print(b.loc[0:1, :]) # slice fails because 0:1 aren't row labels

# setitem with integer and loc

# getitem with strings and iloc
print(a.iloc["0", 0]) # fails because "0" can't be used with iloc
# print(b.iloc["2012-01-02", 0]) # fails because "2012-01-02" can't be used with iloc
# print(a.iloc["0":"2", 0]) # fails because "0":"2" can't be used with iloc
print(b.iloc["2012-01-02":"2012-01-04", 0])

# setitem with strings and iloc
# a.iloc["0":"2"] = 0
# b.iloc["2012-01-02":"2012-01-04"] = 0

# Multiindex
arrays = [['baz', 'baz', 'foo', 'foo', 'bar', 'bar', 'qux', 'qux', 'lux', 'lux'],
          ['red', 'red', 'blue', 'blue', 'red', 'red', 'blue', 'red', 'red', 'blue']]
b = pd.DataFrame({'A': range(10),
                  'B': range(10),
                  'C': range(10)},
                  index=pd.MultiIndex.from_arrays(arrays, names=('number',
                                                                 'color')))
print(b)
print(b.loc['baz', :])
print(b.iloc['baz', :])
