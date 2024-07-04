#Replace all odd numbers in arr with -1 without changing arr
import numpy as np
arr=np.array([11,22,33,44,55,66,77,88,99])
arr1=np.copy(arr)
arr1[arr1%2!=0]=-1
print("Original array:",arr)
print("New array:",arr1)


