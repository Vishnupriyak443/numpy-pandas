#16. Print or show only 3 decimal places of the numpy array rand_arr.
#Hint: numpy. set_printoptions()
import numpy as np
rand_arr=np.random.rand(2,2)
np.set_printoptions(precision=3)
print(rand_arr)
