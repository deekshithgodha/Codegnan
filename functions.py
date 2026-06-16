#function()
#A function is a block of organized, reusabale code and that is used to perform a single or multiple tasks
#python gives i  bulilt function like print, you can make your own function aslo and these are called user defined function
#Fucntion blocks begin with the key word def followed by the function name and peranthesis (()).
'''a=10
b=20
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)
a=100
b=200
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)
a=1000
b=2000
print("The sum is",a+b)
print("The diff is",a-b)
print("The product is",a*b)'''

#function()
'''def deekshith (a,b):
    print("The sum is",a+b)
    print("The diff is",a-b)
    print("The product is",a*b)
deekshith(10,20)
deekshith(100,200)
deekshith(1000,2000)'''

'''while True:
    def deekshith (a,b):
        print("The integer devison is",a//b)
        print("The power is",a**b)
        print("The product is",a%b)
    a=int(input("Enter the A value"))
    b=int(input("Enter the B value"))
deekshith(a,b)'''

#User input
'''def deekshith ():
    a=int(input("Enter the A value"))
    b=int(input("Enter the B value"))
    print("The integer devison is",a//b)
    print("The power is",a**b)
    print("The Modilo divison is",a%b)
deekshith()'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''while True:
    def add():
        a=int(input())
        b=int(input())
        print(a+b)
     add()'''

'''def add():
    a=int(input("Enter the A value"))
    b=int(input("Enter the B value"))
    print(a+b)
    #add()   #Dont write under the print statement.
add()'''


'''def fullname():
    fname=input("First name")
    lname=input("Last name")
    print((fname+" "+lname).title())
fullname()'''

#Task
#Method-1
                     
'''def task ():
    a=int(input("Enter the A value"))
    b=int(input("Enter the B value"))
    option=int(input(Choose the option
                                    1.add
                                    2.sub
                                    3.mul))
    if option==1:
        print("Addition is=", a+b)
    elif option==2:
        print("Subtracton is=",a-b)
    elif option==3:
        print("Multiplication is=",a*b)
task()'''

#method
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("A value"))
    b=int(input("b value"))
    option=int(input(Choose the option
                                    1.add
                                    2.sub
                                    3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
    else:
        print("Check your option")'''

    
#2.nd Task
'''def nani ():
    a=int(input("Enter the person"))
    b=int(input("Enter the amount"))
    print("Per head is",b//a)
nani()'''

'''while True:
    def nani():
        a=int(input("No of numbers"))
        b=int(input("The amount is"))
        print("per head bill is{}".format(b//a))
        print(f"Per head is {b//a}")
    nani()'''

'''while True:
    def nani():
        a=int(input("No of numbers"))
        b=int(input("The amount is"))
        c=b//a
        print("per head bill is{}".format(c))
        print(f"Per head is {c}")
    nani()'''


'''def nani():
    a=int(input("No of numbers:"))
    b=int(input("The amount"))
    print("Per head {}".format(b//a))
nani()'''

#With Varible

'''def nani():
    money=int(input("Enter the money"))
    members=int(input("Enter the Members:"))
    share=money/members
    print("Each person:",share)
nani()'''

'''def nani():
    print("each person gets:",10000/10)
nani()'''

#a=[7,18,12,15,2,4,17]
'''for i in range(len(a)):
    if i%2==0:
        print(a[i])'''

'''for i in a:
    d=a.index(i)
    int(d)
    if d%2==0:
        print(i)'''
'''for i in a:
    d=a.index(i)
    int(d)
    if d%2==0:
        if i%2!=0:
            print(i)'''
'''n=int(input("Enter the number:"))
for i '''

        
#Diffrence b/w print and return
#Print just shows the human user input in console. #built in function
#Return will terminate the functiona and gives back a value from the function #key-word

'''def add(a,b):
    print(a+b)
add(4,5) #Not print '''

'''def add(a,b):
    return(a+b)
print(add(2,3))'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(2,3)'''

def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
   # return d
    return e,d,c
print(add(4,5))









            






    

      
