import numpy as np
import pandas as pd
ls=[1,2,3,4,5,6,7,8]
arr=np.array(['A','C','E','G','H'])
dict={'a':10.5,'b':20,'c':'XYZ','d':40,'e':True}
x=100
s1=pd.Series(ls,index=['a','b','c','d','e','f','g','h'],name="list")
s2=pd.Series(arr)
s3=pd.Series(dict)
s4=pd.Series(x)
s5=pd.Series(s2)
print(s1,"\n",s2,"\n",s3,"\n",s4,"\n",s5) 
tup=(1,2,3)
index=['a','b','c']
s6=pd.Series(tup,index=index)
print(s6)
l=[3,5,7,9,11,13,15,17]
s7=pd.Series(l)


#SERIES ATTRIBUTES
print("Values:",s1.values)
print("Index:",s1.index)
print("Dtype:",s3.dtype)
print("Nmae:",s1.name)
print("Size:",s3.size)
print("Shape:",s3.shape)
print(" Empty:",s7.empty)
print(" Empty:",s4.empty)
print("Ndim:",s2.ndim)
print("Axes:",s3.axes)
print("iat:",s1.iat[2])
print("at:",s1.at['b']) 
print("loc:",s1.loc['c'::2])
print("iloc:",s1.iloc[3::])
print("dtype",s3.dtypes)
print("is_Monotonic:",s7.is_monotonic_increasing)
print("is_Monotonic:",s7.is_monotonic_decreasing)
print("is unique:",s2.is_unique)
print("Has NaNs:",s6.hasnans)

#INDEXING
s = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
# Accessing a single element by index label
print(s['B'])
print(s[1])
print(s.iloc[3])
print(s[[2,3,4]])
print(s[['A','C','E']])
#CONDITIONAL INDEXING
print(s[s>35])

#SLICING
print(s['C':'E'])
print(s[1::2])

#HEAD() FUNCTION
ser=pd.Series([1,2,3,'4','5',6.90,7,8,'A','XYZ'])
print(ser.head(8))
print(ser.tail(6))


print()
# Creating two Series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
# Addition
addition = s1 + s2
print("Addition:\n", addition)
# Subtraction
subtraction = s1 - s2
print("Subtraction:\n", subtraction)
# Multiplication
multiplication = s1 * s2
print("Multiplication:\n", multiplication)
# Division
division = s1 / s2
print("Division:\n", division)
# Exponentiation
exponentiation = s1**2
print("Exponentiation:\n", exponentiation)
# Modulus
modulus = s2 % s1
print("Modulus:\n", modulus)
#COMPARISION OPERATIONS
s=pd.Series([2,32,12,51,31])
s0=pd.Series([21,32,6,78,23])
print(s>s0)
print(s<s0)
print(s<=s0)
print(s>=s0)
print(s==s0)
print(s!=s0)
#FUNCTIONS ON SERIES
sum=s1.sum()
mean=s1.mean()
median=s1.median()
min=s1.min()
max=s1.max()
print("SUM:",sum)
print("MEAN:",mean)
print("Median:",median)
print(f"Min:{min} \n Max:{max}")
std_dev = s1.std()
print("Standard Deviation:", std_dev)
count =s1.count()
print("Count:", count)
# Describe
description =s1.describe()
print("Description:\n", description)

print()
cube=s1.apply(lambda x: x**3)
print("Cube values:",cube)
sqr=np.sqrt(s1)
print("square:",sqr)
