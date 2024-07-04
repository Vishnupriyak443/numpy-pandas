import pandas as pd
s1=pd.Series([39,41,42,44],index=['A','B','C','D'])
x=10
s2=pd.Series(x,index=['A','B','D','F'])
print(s1[:2]*100)
print(s1*s2)
print(s2[::-1]*10)


