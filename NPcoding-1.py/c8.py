# Stack arrays a and b vertically
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([['a','b','c'],['d','e','f']])
vstack=np.vstack((a,b))
print("Verical stack:",vstack)
hstack=np.hstack((a,b))
print("Horizontal stack:",hstack)