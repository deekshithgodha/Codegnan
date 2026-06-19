#Genarator
#No tuple comprehnsion in above cases if we remove those braces and keep the paranthsis and outcome generator

'''a=(i for i in range(16))
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(a)

#We can't we use the both at a same time print(*a) and print(list(a)) .we can  use only one print statement only
print(*a)
print(type(a))

#print(list(a))
#print(tuple(a))
print(set(a))'''

# A Genarator is also a function which can be used as an iterator (loops) by producing groupmof value where we use yield key word
#Yield vs Return
#Return will terminate the function where as yield can pass the function go on with every successive iteration

'''a,b=[int(x) for x in input("Enter the values").split(",")]
def data(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*data(a,b))
'''

'''a,b=[int(x) for x in input("Enter the values").split(",")]
def data(a,b):
    while a<b:
        #yield a
        a=a+1
        return a
    #dont keep the values * in the function calling, its add the a+1 only
print(data(a,b))'''

#yield vs return
'''def mygen():
    #return "python"
    #return "java"
    #return "c"
    #return "python","java","c"
print(*mygen())'''

def mygen():
    yield "vij"
    yield "hyd"
    yield "vzg"
print(*mygen())

#Next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))





