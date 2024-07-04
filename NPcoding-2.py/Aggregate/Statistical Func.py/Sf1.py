#1. Generate a NumPy array of random numbers and find the sum of all
import numpy as np
arr=np.random.rand(2,3)
print(arr)
print(np.sum(arr))

print()
#2. Create a NumPy array of numbers and find the mean of all elements.
arr=np.random.rand(2,3)
print(np.mean(arr))

print()
#3. Generate a NumPy array of numbers and find the median of all.
arr=np.array([10,20,30])
print(np.median(arr))

print()
#4. Create a NumPy array of numbers and find the minimum value.
arr=np.array([51,20,30,45,32,82,12,19])
print(np.min(arr))

print()
#5. Generate a NumPy array of numbers and find the maximum .
arr=np.array([51,20,30,45,32,82,12,19])
print(np.max(arr))

print()
#6. Create a NumPy array of numbers and find the standard
arr=np.array([51,20,30,45,32,82,12,19])
print(np.std(arr))

print()
#7. Generate a NumPy array of numbers and find the variance.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.var(arr))

print()
#8. Create a NumPy array of numbers and find the sum of all elements along a specific axis.
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print("Horizontal:",np.sum(arr,axis=0))
print("Vertical:",np.sum(arr,axis=-1))
print("axis=1:",np.sum(arr,axis=1))

print()
#9. Generate a 2D NumPy array of random numbers and find the mean of each row with axis parameter.
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print("Row-wise:",np.mean(arr,axis=-1))

print()
#10. Create a 2D NumPy array of numbers and find the median of each column with axis parameter.
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print("column-wise:",np.median(arr,axis=0))

print()
#11. Generate a 2D NumPy array of numbers and find the minimum value in each row using `numpy.min` with axis parameter.
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print(np.min(arr,axis=-1))

print()
#12. Create a 2D NumPy array of numbers and find the maximum value in each column with axis parameter.
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print(np.max(arr,axis=0))

print()
#13. Generate a 2D NumPy array of numbers and find the standard deviation of each column with axis parameter
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print(np.std(arr,axis=0))

print()
#14. Create a 2D NumPy array of numbers and find the variance of each row with axis parameter
arr = np.array([[13,22, 43], [34, 15, 96], [37, 28,91]])
print(np.var(arr,axis=-1))

print()
#15. Generate a NumPy array of random numbers and find the index of the minimum value
arr=np.random.rand(2,3)
print(arr)
print(np.argmin(arr))

print()
#16. Create a NumPy array of numbers and find the index of the maximum
arr=np.random.rand(2,3)
print(arr)
print(np.argmax(arr))

print()
#17. Generate a 2D NumPy array of random numbers and find the index of the minimum value along a specific axis with axis parameter.
arr=np.random.rand(2,3)
print(arr)
print("Column-wise:",np.argmin(arr,axis=0))
print("Row-wise:",np.argmin(arr,axis=-1))

print()
#18. Create a 2D NumPy array of numbers and find the index of the maximum value along a specific axis with axis parameter.
arr=np.random.rand(2,3)
print(arr)
print("Column-wise:",np.argmax(arr,axis=0))
print("Row-wise:",np.argmax(arr,axis=-1))

print()
#19. Generate a NumPy array of random integers and count the number of occurrences of each unique value using `numpy.bincount`
arr=np.random.randint(0,5,size=10)
print(arr)
count=np.bincount(arr)
print("count:",count)
#unique=np.unique(np.sort(arr))
#print(unique)
#for i in unique:
    #print(f"{i} occurred at ")
    #for j in count:
        #print(f" {j} times")
        
for i in range(len(count)):
    print(f"{i} counts:{count[i]}")        








print()
#20. Create a NumPy array of numbers and compute the cumulative sum of the elements
arr=np.random.rand(2,3)
print(arr)
print(np.cumsum(arr)) 

print()
#21.create a 8*8 matrix and fill it with a checkboard pattern
x = np.zeros((8, 8), dtype=int)
x[1::2, ::2] = 1  
x[::2, 1::2] = 1  
print(x)

print()
#22.create a 2d array with 1 on the border and 0 inside
arr=np.ones((6,6))
arr[1:-1,1:-1]=0
print(arr)

