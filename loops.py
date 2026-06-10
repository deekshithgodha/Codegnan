 #loops()
#for, while,range,break, continue,pass
#for loop()
'''a=[10,20,30,40,50]
for i in a:
    print(i)
    '''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#list
'''a=(1,2,3,4,5)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#dictionary
'''a={1,2,3,4,5,6}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"Deekshith","year":2026,"month":6}
for i in a:
    print(i)
    print(type(a))
    print(type(i))
for i in a.keys():
    print(i)
    print(type(a))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[4,6.7,"python",6+9j,True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i,end="")
    print(type(a))
    print(type(i))'''

'''fruits=["apple","mango","grapes"]
for i in fruits:
    print(i,end'=",")'''


'''b=str(a)
print(b.upper())'''

'''a=["codegnan","python","course"]'''
'''for i in a:
    print(i.upper(),end=",")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#While loop()
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''

'''a=20
while a>5:
    print(a)
    a=a-1'''

#Running the number infinty
'''a=20
while a>6:
    print(a)
    a+=1'''

#voting while loop using
'''while True:
    age=int(input("Enter the age:"))
    if age>=18:
        print("Eligible for vote")
    else:
        print("Not Eligible for vote")'''


'''while  True:
    age=int(input("Enter the age:"))
    marks=int(input("Enter the marks:"))
    attendence=int(input("Enter the attendence:"))
    if age >= 18:
        print("they are Eligible for vote")
    if marks >=80:
        print("Eligible for write exmas")
    if attendence >=90:
        print("Eligible for schorlship")'''


#Range function is return a seques of a number, staring from the 0 for default, and increments by one by one ,and stops before a specified number
#range()
#Start-Stop-Step
'''for i in range(10):
    print(i)'''

'''for i in range(1,101):
    print(i)'''

'''for i in range(0,28,3):
    print(i)'''

'''for i in range(2,20,2):
    print(i)'''
    
''' i in range(5,50,5):
    print(i)'''

'''marks=int(input("Enter the marks"))
if marks in range(91,101):
    print("Grade-A")
elif marks in range (81,91):
    print("Grade-B")
elif marks in range(71,81):
    print("Grade-C")
elif marks in range(50,71):
    print("Grade-D")
else:
    print("Fail,Study Well...")'''

#Break()
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==7:
        break'''

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break
print(a)'''


'''a=20
while a>5:
    print(a)
    a=a-1
    if a==8:
        break'''

'''for i in range(20):
    if i==13:
        break
    print(i)'''


'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#Continue

'''a=30
while a>10:
    a=a-1
    if a==19:
        continue
    print(a)'''

'''a=40
while a>15:
    a=a-1
    if a==25:
        continue
    print(a)'''


'''for i in range(25):
    if i==17:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''

#pass
'''a=15
while a>10:
    print(a)
    a=a-1
    if a==14:
        pass'''

'''for i in range(20):
    if i==15:
        pass
    print(i)'''

#Task's

'''a=40
while a>10:
    a=a-1
    if  a==28:
        continue
    if  a==19:
        break
    print(a)'''


'''a=int(input("Enter the student number"))
b=list(map(str,input().split()))
present =0
absents=0
print("Total",a)
for i in b:
    if i=="p":
        present +=1
    if i=="a":
        absents+=1
print("Present:", present)
print("Absents:",absents)'''

#Student  Attendence Report
student=int(input("Enter the no.of students"))
p=0
a=0
for i in range(1,student+1):
    b=input(f"student attendence {i} p or a")
    if b=="p":
        p+=1
    elif b=="a":
        a+=1
print(".........Attendence Report..................")
print("total students:", student)
print("total presenties:",p)
print("total absenties:",a)
        
            

    
    
        
    
    


    




    
    
        
