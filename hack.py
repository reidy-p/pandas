import pandas as pd 

s = pd.Series(range(5), index=pd.date_range("2012-01-01", periods=5))
s = pd.DataFrame({'A': range(5),
                  'B': range(5), 
                  'C': range(5)}, 
                  index=pd.date_range("2012-01-01", periods=5))

s.loc["2012-01-02":"2012-01-04"]

s.iloc["2012-01-02":"2012-01-04"]

s.iloc[3, 0]
s.iloc[3.0, 2]