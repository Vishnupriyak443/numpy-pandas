#7. Generate a NumPy array of numbers with decimals and round all the elements to the nearest multiple of 10.
import numpy as np
arr=np.array([20.342,3.333,43.89097,54.943,133.72,62.43,7.3245])
x=np.round(arr,decimals=-1)
print(x)
