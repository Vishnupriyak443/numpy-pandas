#10. Create a NumPy array of numbers with decimals and round all the elements to the nearest multiple of 0.5.
import numpy as np
arr=np.array([20.342,3.333,43.89097,54.943,133.72,62.43,7.3245])
x=np.round(arr/0.5)*0.5
print(x)

