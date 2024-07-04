#7. Given two arrays `arr1` and `arr2`, check if they are element-wise equal
import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([9,2,4,6,5])
print("Equal:",np.equal(arr1,arr2))

print()
#8. Given an array `arr`, count the number of non-zero elements
arr=np.array([0,1,2,3,4,5])
print(np.count_nonzero(arr))

print()
#9. Given an array `arr`, find the indices where the values are non-zero.
arr=np.array([2,0,4,0,5,0,1,0]) 
print(np.nonzero(arr))

print()
#10. Given two arrays `arr1` and `arr2`, 
#check if all corresponding elements in `arr1` are less than or equal to the corresponding elements in `arr2`.
arr1=np.array([7,2,3,9,5])
arr2=np.array([2,1,4,6,5])
print((arr1<=arr2))

print()
#11. Given an array `arr`, check if all elements are finite (not NaN or infinite).
arr=np.array([10,20,30,40,50,60])
print(np.all(arr>=0), "Finite")

print()
#12. Given two arrays `arr1` and `arr2`, check if any corresponding elements in `arr1` are equal to the corresponding elements in `arr2`
arr1=np.array([7,2,3,9,5])
arr2=np.array([2,1,4,6,5])
print(np.equal(arr1,arr2))

print()
#13. Given an array `arr`, check if it contains any duplicate elements
arr=np.array([1,2,5,3,4,1,5])
unique,count=np.unique(arr,return_counts=True)
print(unique)
print(count) #Return counts of each elements
print("Duplicates:",np.any(count>1))



print()
#14. Given an array `arr`, calculate the mean value of the array
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print("Mean:",np.mean(arr))

print()
#15. Given an array `arr`, check if all elements are within a specified range `[min_val, max_val]`.
arr=np.array([23,41,28,11,45,12,18])
range=[10,20]
print(np.all(arr>=10)&(arr<=35))


print()
#16. Given an array `arr`, find the indices where the values are equal to a specified value `value`.
arr=np.array([50,10,20,30,40])
value=20
#print("Equal:",np.all(np.equal(arr,value)))
print("Equal:",np.where(arr==value))



print()
#17. Given two arrays `arr1` and `arr2`, check if all corresponding elements in `arr1` are greater than the corresponding elements in `arr2`.
arr1=np.array([7,2,3,9,5])
arr2=np.array([2,1,4,6,5])
print(np.greater(arr1,arr2))

print()
#18. Given an array `arr`, find the indices of the top n minimum values in the array.
arr=np.array([11,2,4,6,43,7,0,1,7])
n=5
arr1=np.sort(arr)
print(f"{n} minimum values are: {arr1[:n]}")



print()
#19. Given an array `arr`, check if all elements are positive
arr=np.array([10,2,8,-1,31,-21,13])
print(np.all(arr>=0))



