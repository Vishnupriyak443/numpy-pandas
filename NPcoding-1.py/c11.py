#. Get all items between 5 and 10 from a.
import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
range=a[(a>5) & (a<11)] 
print(range)