#Universal Functions
import numpy as np
a=np.array([1,2,3])
b=np.array([[1],[2],[3]])
result=a+b
print(result)

print()
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2],[3,4],[5,6]])
#result=a+b
#print(result)
a=np.random.rand(6,7)
b=np.random.rand(7,6)

#Arithmetic Operations
x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])
add=x+y 
print("Addition:",add)
print("Subtraction:",x-y)
print("Multiply:",x*y)
print("Division:",x/y)
print("Exponentiation:",x**y)
print("Modulo:",y%x)

#Trignometric Functions
arr=np.array([0,30,45,90,180,270,360])
sin_arr=np.round(np.sin(np.radians(arr)),2)
print("Sin arr:",sin_arr)
cos_arr=np.round(np.cos(np.radians(arr)),2)
print("Cos arr:",cos_arr)
tan_arr=np.round(np.tan(np.radians(arr)),2)
print("tan arr:",tan_arr)
arccos_arr=np.round(np.arccos(np.radians(arr)),2)
print("arccoss_arr:",arccos_arr)
arcsin_arr=np.round(np.arcsin(np.radians(arr)),2)
print("Arcsin_arr:",arcsin_arr)
arctan_arr=np.round(np.arctan(np.radians(arr)),2)
print("Arctan_arr:",arctan_arr)
degree=np.sin(np.radian())



