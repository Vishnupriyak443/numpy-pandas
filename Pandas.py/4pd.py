import pandas as pd
s=pd.Series([95,89,92,95],['PI','Physics','Chemistry','Math'])
print(s.iat[0])
print(s['PI'])
print(s.at['PI'])
print()
increase=s+10
print(increase)
