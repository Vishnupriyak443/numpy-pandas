#Single line if ekse statement 
import numpy as np
import pandas as pd
x=58
result = {x > 0: "Positive", x < 0: "Negative"}.get(True, "Zero")
print(result)
res={x%2==0:"EVEN", x%2!=0:"Odd"}.get(True,"Zero")
print(res)
x1=23
res1="Even" if x1%2==0 else "Odd"
print(res1)


print()
age=10
age_group = "Minor" if age < 18 else "Adult"
print(age_group)


print()

s=pd.Series(200,index=range(10,15))
print(s)
s1=pd.Series([10,20,30,40,50])
s1.index=range(0,5)
print(s1)
s2=pd.Series(np.arange(10,15))
print(s2)
s1[0]=100
s1[1:4]=-23.43
print(s1)
data=np.arange(5.25,50.0,10.25)
index=['a','b','a','a','b']
ser=pd.Series(data,index=index)
print(ser)
print(ser['a'])
print(ser['b'])
