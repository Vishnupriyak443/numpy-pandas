#18. From the array a, replace all values greater than 30 to 30 and less than 10 to 10
import numpy as np
a=np.array([11,2,30,48,56,13,8,7,15,9])
a[a>30]=30
a[a<10]=10
print(a)