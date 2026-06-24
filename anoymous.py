#anoymous
'''#are functios are name less functions and we use a key word as lamda to create functions
def function(x):
    return (2*x+5)
x=int(input())
print(function(x))


#syntax
#a=lambda arg:expr
a=lambda x:2*x+5
print(a(5))


a=int(input())
b=lambda x:2*x+5
print(b(a))


a=input()
b=lambda x:x.upper()
print(b(a))


a=input()
b=lambda x:x.title()
print(b(a))


a=int(input())
b=int(input())
c=lambda x,y:x*y
print(c(a,b))



a=input()
b=input()
c=lambda x,y:(x+" "+y).title()
print(c(a,b))



a,b=[x for x in input().split(",")]
c=lambda x,y:(x+" "+y).title()
print(c(a,b))


#filter()
a=[2,8,10,13,15,17,20,23,25,50,80,90,100]
b=list(filter(lambda x:x%2==0,a))
print(b)


#[],(),{}
a=[]
print(type(a))
b=()
print(type(b))
c={}
print(type(c))
d=set()
print(type(d))


a=[[],(),set(),{},"",None,4,6.7,"python",4+9j,True,False]
b=list(filter(None,a))
print(b(a))

#map()->each object from a collection and forms a new collection
a=[2,6,8,9,10,20,5,60]
b=[1,4,7,12,14,70,80,90]
c=list(map(max,a,b))
print(c)


d=list(map(min,a,b))
print(d)


#map()
a=input()
b=input()
print(a+b)


a,b=input().split(",")
print(a+b)


a,b=[x for x in input().split(",")]
print(a+b)


a,b=map(str,input().split(","))
print(a+b)


a=int(input())
b=int(input())
print(a+b)


a,b=[int(x) for x in input().split(",")]
print(a+b)


a,b=int(input().split(","))
print(a+b)#error


a,b=map(int,input().split(","))
print(a+b)


a=list(map(int,input().split(",")))
print(a)


a=tuple(map(int,input().split(",")))
print(a)


a=set(map(int,input().split(",")))
print(a)


a=list(map(str,input().split(",")))
print(a)


d = {}
key = input("Enter key: ")
value = input("Enter value: ")
d[key] = value
print(d)


a=input()
b=dict(i.split(":") for i in a.split(","))
print(b)

#ASCII
#chr
print(chr(56))
print(chr(90))
print(chr(65))
print(chr(91))m
for i in range(65,91):
    print(chr(i),end=" ")
for i in range(97,123):
    print(chr(i),end=" ")
#ord
print(ord("a"))
print(ord("z"))

a=input()
for i in a:
    print(f"{i} : {ord(i)}",end=" ")'''


