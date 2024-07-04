#1. Generate two NumPy arrays of the same shape and add them element-wise.
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(a+b)

print()
#2. Create two NumPy arrays of the same shape and subtract one from the other element wise.
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
sub=np.subtract(a,b)
print(sub)

print()
#3. Generate two NumPy arrays of the same shape and multiply them element-wise
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(a*b)

print()
#4. Create two NumPy arrays of the same shape and divide one by the other element-wise.
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
print(a/b)

print()
#5. Generate a NumPy array and add a scalar value to all its elements.
a=np.array([11,22,33,44,55])
print((a+5))

print()
#7. Generate a NumPy array and multiply all its elements by a scalar value.
a=np.array([11,22,33,44,55])
print((a*5))

print()
#8. Create a NumPy array and divide all its elements by a scalar value.
a=np.array([10,22,30,44,50])
print((a/5))

print()
#9. Generate two NumPy arrays of different shapes and perform matrix multiplication between them.
arr=np.array([[1,2,3],[4,5,6]])
arr1=np.array([1,2,3])
mult=np.multiply(arr,arr1)
print(mult)

print()
#10. Create a NumPy array and raise all its elements to a certain power
arr=np.array([[1,2,3],[4,5,6]])
print((arr**5))

print()
#11. Generate a NumPy array and calculate the square root of all its elements.
arr=np.array([[11,12,13],[14,15,16]])
print(arr**2)

print()
#12. Create a NumPy array and calculate the exponential of all its elements.
arr=np.array([[1,2,3],[4,5,6]])
print(3**arr)

print()
#13. Generate a NumPy array and calculate the natural logarithm of all its elements
arr=np.array([10,20,30,40,50])
log=np.logspace(arr,stop=1,num=5)
print(log)

print()
#14. Create a NumPy array and calculate the logarithm base 10 of all its elements.
arr=np.array([10,20,30,40,50])
log=np.logspace(arr,stop=10,num=5)
print(log)

print()
#15. Generate two NumPy arrays of the same shape and find the maximum value between corresponding elements.
arr=np.array([42,31,53,26,78])
arr1=np.array([33,55,21,16,84])
print(np.maximum(arr,arr1))

print()
#16. Create two NumPy arrays of the same shape and find the minimum value between corresponding elements.
arr=np.array([42,31,53,26,78])
arr1=np.array([33,55,21,16,84])
print(np.minimum(arr,arr1))





