#Extract all odd numbers from array.
import numpy as np
arr=np.arange(0,10)
print(arr)
odd_num=arr[arr%2!=0]  #Boolean indexing
print(odd_num)