#Generate a Python list of all the even numbers between 4 to 30
def even_Num( ):
    ls=[]
    for i in range(4,30):
        if(i%2==0):
            ls.append(i)
    return ls
list=even_Num()
print(list)