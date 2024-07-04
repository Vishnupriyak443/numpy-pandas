import numpy as np
a1= np.array([10,20,30]) #1D-Array
print(a1)
print(a1.size)
print(a1.dtype)
a2=np.array([[11,22],[110,220]],dtype=float) #2D-Array
print(a2)
a3=np.array([  
    [[1,2,3],     
    [10,20,30]],
    [[100,200,300],
     [1000,2000,3000]]
])                          #3D-Array
print(a3)
#Attributes 
print("a2 .size:",a1.size)
print("a2.shape:",a2.shape)
print("N-dimensions:",a2.ndim)
print("a3.shape:",a3.shape) 
print("a3.dtype:",a3.dtype)
print("a2.itemsize:",a2.itemsize) 
print("a3.nbytes:",a3.nbytes) 
print("a1.flags:",a1.flags)
print("Transpose",a2.T)
a4=np.array([[2+3j],[4+5j]])
print("Imaginary items:",a4.imag)
print("Real items:",a4.real)
