#program to create recursive function to calculate the sum of numbers from 0 to 10.
def recFun(*x):
    add=0
    for i in x:
        add+=x[i]
    return add
sum=recFun(0,1,2,3,4,5,6,7,8,9,10)    
print(sum)
