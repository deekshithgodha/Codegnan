#keyword and positional arguments
#Step1
'''def Details(id,name,mailid):
    id=10
    name="Deekshith"
    mailid="deekshith@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
    #step2
Details(id="id",     name="name",mailid="mailid")
#Step3
Details(id="20",    name="Deekshith",mailid="deekshith@gmail.com")
Details(id="30",    name="Deekshithaa",mailid="deekshithaa@gmail.com")
#step4
Details(40,"nani",  "nani@gmail.com")
Details("Anadh",    "a@gamil.com",50)
#step5
Details(mailid="buddi@gmail.com",name="Buddi",id="70")'''

#Swapinng
'''a=10
b=20
a,b=20,10
print("value of a",a)
print("value of b",b)'''

#Method-2
'''a=20
b=10
temp=a
a=b
b=temp
print(a,b)'''

'''def swap(a,b,temp):
    a=10
    b=20
    temp=0
    temp=a
    a=b
    b=temp
    print(a,b,temp)
swap(a="a",b="b",temp="temp")'''

#Method-3
'''a=20
b=10
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''

#Method-4
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("After the swapping a=%d, b=%d"%(a,b))'''

#Default arguments
#method-1
'''def Grocery(item,price):
    print("Item is %s" %item)
    print("Price is %.2f" %price)
Grocery("sugar",100)'''

#MEthod -2
'''def Grocery(item="Rice",price=1500):
    print("Item is %s" %item)
    print("Price is %.2f" %price)
Grocery()'''

#Method-3
''' Grocery(item,price=200):
    print("Item is %s" %item)
    print("Price is %.2f" %price)
Grocery("Dhal")'''

#method-4
'''def Grocery(item="Ghee",price):
    #Non-Default argument follows the default arguments
    print("Item is %s" %item)
    print("Price is %.2f" %price)
Grocery(500)'''

#----TASK---------
     #Method-1
'''def bakary(cake,price,quantity):
    print("Item is %s" %cake)
    print("Price is %.2f" %price)
    print("Price is %s" %quantity)
bakary("Butter-Stocth",400,4)'''

#Method-2

'''def bakary(cake="Vennela",price=400,quantity=1):
    print("Item is %s" %cake)
    print("Price is %.2f" %price)
    print("Price is %s" %quantity)
bakary()'''

#Method-3

'''def bakary(cake,price=350,quantity=1):
    print("Item is %s" %cake)
    print("Price is %.2f" %price)
    print("Price is %s" %quantity)
bakary("Chocolate",)'''

#Method-4 
'''def bakary(cake="Cream",price,quantity):
    print("Item is %s" %cake)
    print("Price is %.2f" %price)
    print("Price is %s" %quantity)
bakary(400,4)'''

#*arguments-> *is used to unpack the elements
#Using List
'''a=[2,3,4,5,6,7]
print(a)
print(type(a))
print(*a)'''

#Using Tuple
'''a=(2,3,4,5,6,7)
print(a)
print(type(a))
print(*a)'''

#Using Dist
'''a={2,3,4,5,6,7}
print(a)
print(type(a))
print(*a)'''

#Dist
'''a={"name":"pooja","year":2026,"month":6}
print(a)
print(type(a))
print(*a)'''

#String 
'''a="codegnan"
print(a)
print(*a)'''

#Error
'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)''' #Value Error

#Normal
'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)''' #a is Started from 2 end with 8 and  b print 9, c is print 10

'''a,b,c="Codegnan"
print(a)
print(b)
print(c)''' #Value error

'''a,b,c="Cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

#Variable Length Arguments
#Variable length arguments are automatically stores in tuple and we use *arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)

b=[3,4,5,6,7]
check(*b)

c=(9,10,11)
check(*c)

d={5,6,7,8,9}
check(*d)

e={"year":2026,"month":"June"}
check(*e)'''

'''def  check1(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(3,4.5,6.7,6.7)
check1(2,3,4,5,2.3,4.5,"Pooja",6+9j,True,False)'''

'''while True:
    def train_ticket():
        ticket=int(input("Enter the Ticket price"))
        gender=input("Enter the Gender").lower()
        age=int(input("Enter the Age"))
        if gender =="male":
            if age>=60:
                discount=ticket-(30*10)
                print("The Person is Senior citizen")
                print("Ticket Dscount is",discount)
            elif age<60:
                print("normal citizen")
                print(discount)
        elif gender=="female":
            if age>=60:
                discount=ticket-(50*10)
                print("The Person is Senior citizen")
                print("Ticket Dscount is",discount)
            elif age<60:
                print("normal citizen")
                print(discount)
    train_ticket()  '''


#kwargs(**)
'''def Details(**a):
    print(a)
    print(type(a))
Details()
d={"idnos":[10,20,30],
   "name":["bhanu","Deekshith","nani"],
   "status":["p","a",:"p"]
print(**d)'''


'''def Details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values:
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
Details()
d={"idnos":[10,20,30],
   "name":["bhanu","Deekshith","nani"],
   "status":["p","a","p"]}
print(**d)'''


'''def final (*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("Keys",i)
        print("Values",j)
final()
d=(1,2,3,4,5,7.9)
final(*d)
e={"idnos":[10,20,30],
   "names":["bhanu","Deekshith","nani"],
   "status":["p","a","p"]}
final(**e)
final(*d,**e)
'''

'''#Max(),Min(),Sum()
print(max(10,20,304,507,209))

#min()
print(min(10,20,394,10,20))

#sum()
a=2,3,4,5,6,7,8
print(sum(a))'''

#--Task__

'''s=int(input("Enter the students"))
for i in range(1,s+1):
    marks=list(map(int ,input().split()))
print(s)
print(max(marks))
print(min(marks))
print(sum(marks)/students)'''

#Student marks analysis report
students=int(input("Enter the Students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"Enter the students {i} students"))
    b=marks.append(mark)
for i in marks:
    print(i)
print("..............Marks Analysis Report...........")
print("Total students",students)
print("Heghest Marks",max(marks))
print("Lowest Marks",min(marks))
print("Total Marks",sum(marks))
print("Average is",sum(marks)/students)

        
        
              
    




