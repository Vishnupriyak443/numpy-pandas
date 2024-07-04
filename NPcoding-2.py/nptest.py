import numpy as np
def func(a,b=[]):
    b.append(a)
print(func(1))
print(func(2))
print(func(3,[]))
print(func(4))    

#dt=np.dtype(('age',np.int8))
arr=np.array([(10,),(20,),(30,)])
#print(a[age])

a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.dot(a,b)
outer=np.outer(a,b)
print("np.dot():",c)
print("np.outer():",outer)


arr=np.array([(10,20,30)])
print(arr)

arr=np.array([1,2,3,4,5],ndmin=2)
print(arr)

a=np.array([[0,1],[2,3]])
print(a.transpose())

a=np.array([[1,2,3],[4,5,6]])
b=np.array([1,0,1])
print(a+b)
a=np.array([[1,2],[3,4]])
b=np.array([1,2])
print(a*b)

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a
x=b is a
print(x)


a=np.array([(10,20,30)])
print(a.itemsize)

print()
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.concatenate((a,b))
print(c)

print()
thistuple = ("apple",)
print(type(thistuple))

print()
a=np.array([1,2,3])
print(np.add(a,1)) #Vectorization





