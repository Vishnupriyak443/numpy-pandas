#9. Generate a NumPy array of numbers with decimals and 
#round all the positive elements up and all the negative elements down using `numpy.fix`.
import numpy as np
arr=np.array([20.342,-3.6533,43.89097,54.943,133.72,-62.33,7.3245])
x=np.fix(arr)
print(x)



