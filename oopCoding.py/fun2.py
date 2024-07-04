def calculation(x,y):
    add=x+y
    if(x>y):
        sub=x-y
    else:
        sub=y-x
    return add,sub
result=calculation(10,20)
print("Additon:",result[0])
print("Subtraction:",result[1])
