#6. Create a NumPy array of numbers with decimals and round all the elements to the nearest even integer
import numpy as np
arr=np.array([20.342,3.333,43.89097,54.943,133.72,62.43,7.3245])
round=np.round(arr)
print(np.any(round,where=round%2!=0))



