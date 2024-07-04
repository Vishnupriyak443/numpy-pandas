#1. Create a null vector of size 10 but the fifth value which is 1.
import numpy as np
a=np.zeros(10)
print(a)
a[4]=1
print(a)

print()

#2. Create a vector with values ranging from 10 to 49.
import numpy as np
a=np.arange(10,49)
print(a)

print()

#3. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
#hint: np.nonzero`
import numpy as np
a=np.array([1,2,0,0,4,0])
indeces=np.nonzero(a)
print(indeces)

print()

#4. Create a 3x3x3 array with random values
import numpy as np
a=np.random.rand(3,3,3)
print(a)

print()
#5. Create a 10x10 array with random values and find the minimum and maximum values.

a=np.random.rand(10,10)
print(a)
print("Minimum of array:",np.min(a))
print("Maximum of array:",np.max(a))

print()

#6. Create a random vector of size 30 and find the mean value.
a=np.random.rand(30)
print("Mean:",np.mean(a))

print()

#7. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
a=np.diag([1,2,3,4],k=-1)
print(a)

print()

#8. Let x be an arbitrary array. Return True if none of the elements of x is zero. Remind that 0 evaluates to False in python.
x = np.array([1,2,3])
x = np.array([1,0,3])
#mask=x.all(where=x!=0)
print(all(x))

print()
#
#9. Let x be an arbitrary array. Return True if any of the elements of x is non-zero.
x = np.array([1,0,2])
y = np.array([3,4,0])
#mask=x.any(where=x>0)
print(any(x))

print()

#10. Write numpy comparison functions such that they return the results as you see.
x = np.array([4, 5])
y = np.array([2, 5])
#[ True False][ True True][False False] [False True]
print("Comparision functions:")
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))

print()

#11. Calculate sine, cosine, and tangent of x, element-wise.
x = np.array([0., 1., 30, 90])
sin_arr=np.round(np.sin(np.radians(x)))
print("Sine_arr:",sin_arr)
cos_arr=np.round(np.cos(np.radians(x)))
print("Cosine_arr:",cos_arr)
tan_arr=np.round(np.tan(np.radians(x)))
print("Tangent_arr:",tan_arr)

print()

#12. Calculate inverse sine, inverse cosine, and inverse tangent of x, element-wise.
x = np.array([-1., 0, 1.])
arcsin_arr=np.round(np.arcsin(np.radians(x)))
print("inverse of sine:",arcsin_arr)
arccos_arr=np.round(np.arccos(np.radians(x)))
print("Inverse of cosine",arccos_arr)
arctan_arr=np.round(np.arctan(np.radians(x)))
print("Inverse of tan:",arctan_arr)

print()

#13. Use array x to get the below output.
x = np.array([2.1, 1.5, 2.5, 2.9, -2.1, -2.5, -2.9])
#Output:
#[ 2. 2. 2. 3. -2. -2. -3.]
#[ 2. 1. 2. 2. -3. -3. -3.]
#[ 3. 2. 3. 3. -2. -2. -2.]
#[ 2. 1. 2. 2. -2. -2. -2.]
#[2.0, 2.0, 3.0, 3.0, -2.0, -3.0, -3.0]
print(np.round(x))
print(np.floor(x))
print(np.ceil(x))
print(np.trunc(x))
print(np.ceil(x) if x>0 else np.floor(x))
#print(mask)



print()

#14. Calculate the difference between neighboring elements, element-wise.
x = np.array([1, 2, 4, 7, 0])
print(np.diff(x))

print()
#15. Create a 1D array and Add 2 to each element of arr1d
arr1d=np.array([1,2,3,4,5,6,7,8])
print(np.add(arr1d,2))



