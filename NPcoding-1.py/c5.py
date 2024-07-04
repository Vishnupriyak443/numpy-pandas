#Replace all odd numbers in arr with -1.
import numpy as np
arr=np.array([11,22,33,44,55,66,77])
arr[arr%2!=0]=-1
print(arr) 