#Get the common items between a and b
import numpy as np
a=np.array([1,'a',4,"xyz",5])
b=np.array(['c',"xyz",3,5])
x=np.intersect1d(a,b)
print("common items:",x)
