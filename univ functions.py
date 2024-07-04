import numpy as np
arr=np.zeros((2,3))
print("Array with zeros:",arr)
arr=np.ones((2,2))
print("Arrays filled with ones:",arr)
arr=np.diag((10,20,30),k=2)
print("Diagonal array:",arr)
arr=np.arange(1,5,1,dtype=int)
print("Array with Range:",arr)
arr=np.linspace(1,2,num=5,endpoint=True,retstep=True)
print("Linespace:",arr)
arr=np.logspace(1,4,num=5,endpoint=True,dtype=int) 
print("Log space:",arr) 
x=np.array([1,2,3])
y=np.array([10,20,30])
x,y=np.meshgrid(x,y)
print("X values:",x)
print("Y values:",y)
arr=np.random.rand(2,3)
print("Array with random elements b/w 0-1:",arr)
arr=np.identity(4,dtype=int)
print("Identity array:",arr)

arr1=np.array([[1,0,0],
              [0,2,0],
              [0,0,3]])
d=np.diag(arr1)  
print("Extracting diag ele:",d)
arr=np.empty((2,3))
print(arr)
arr=np.eye(4,5,k=1)
print("np.eye():",arr)
empty_array = np.empty((2, 3))
print("Empty array",empty_array)
#Fromfunction
def func(i, j):
 return i + j
# Create a 3x3 array using np.fromfunction
from_func_array = np.fromfunction(func, (2, 3), dtype=int)
print("Array created using np.fromfunction:")
print(from_func_array)
#Indexing & Slicing
arr = np.array([1, 2, 3, 4, 5]) #Indexing 1D array
print(arr[0]) 
arr = np.array([[1, 2, 3], [4, 5, 6]]) #Indexing 2D array
print(arr[0, 1]) 
arr = np.array([[[1, 2, 3],
 [4, 5, 6]],
 [[7, 8, 9],
 [10, 11, 12]]])        #Indexing 3Darray
# Accessing the element at depth 0, row 1, column 2
print(arr[0, 1, 2]) 

#SLICING
print("slicing:")
arr = np.array([1, 2, 3, 4, 5])
print(arr[3])
print(arr[-4])
print(arr[1:5])
print(arr[:])
print(arr[0:-1])
print(arr[:5])
print(arr[2:-1])
print(arr[1:5:1])
print(arr[::-1])
print("multi-dimensional slicing:")
a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2[0:3,1:])
print(a2[-2:,0:])
a3=np.array([[[10,20,30],
            [40,50,60]],
            [[100,200,300],
            [400,500,600]]])
print(a3[1,0,1]) 
