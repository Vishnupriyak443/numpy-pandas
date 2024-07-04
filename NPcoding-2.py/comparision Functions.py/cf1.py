#1. Given an array `arr`, find the maximum value in the array
import numpy as np
arr=np.random.rand(2,3)
print("arr",arr)
print("max:",np.max(arr))

print()
#2. Given an array `arr`, find the minimum value in the array.
arr=np.random.rand(2,3)
print("arr:",arr)
print("Min:",np.min(arr))

print()
#3. Given an array `arr`, determine the indices of the maximum and minimum values.
arr=np.random.rand(3,3)
print("arr:",arr)
print("Index of minimum:",np.argmin(arr))
print("Index of maximum:",np.argmax(arr))

print()
#4. Given an array `arr` and a threshold value `threshold`, check if any element in the array is greater than the threshold
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
threshold=40
print(np.any(arr>threshold))

print()
#5. Given an array `arr` and a threshold value `threshold`, check if all elements in the array are less than the threshold
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
threshold=40
print(np.all(arr<threshold))

print()
#6. Given an array `arr`, count the number of elements greater than a specified value `value`.
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
value=20
l=np.len(arr)
print(" Length",l>value  ) ############################

print()
#7. Given two arrays `arr1` and `arr2`, check if they are element-wise equal
arr1=np.array([1,2,3,4,5])
arr2=np.array([9,2,4,6,5])
print("Equal",np.equal(arr1,arr2))

print()
