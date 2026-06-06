#if-condition by using comparasion operators
#<,>,<=,>=,!=,==

'''a= 10
if a>1:
    print("True")'''


'''a= 10
if a<1:
    print("True")'''

'''a= 20
b=30
if a<b:
    print("True")'''

'''a= 5
b=7
if a<=b:
    print("True")'''


'''a= 15
b=7
if a>=b:
    print("Greater")'''


'''a= 3
b=6
if a!=b:
    print("not equal")'''

'''a= 3
b= 8
if a!=b:
    print("not equal")'''

'''a= 3
b= 3
if a==b:
    print("equal")'''

'''a= int(input("a value:"))
b= int(input("b value:"))
if a>b:
    print("Greater")'''

'''a= int(input("a value:"))
if a!=20:
    print("True")'''

'''a= "python"
if a=="python":
    print("True")'''

'''a= input("data:")
if a=="python":
    print("True")'''

#if - condition by using logical operator
#and,or,not
'''a=2
b=4
if a<b and b>a:
    print("True")'''

'''a=2
b=4
if a<b and b<a:
    print("True")'''

'''a=5
b=7
if a<=b and b>=a:
    print("True")'''

'''a=6
b=7
if a<=b and b>=a:
    print("True")'''

'''a=9
b=11
if a!=b and b==a:
    print("True")'''

'''a=1
b=3
if a<b and b>a:
    print("True")'''

#or condition

'''a=3
b=6
if a!=b or b==a:
    print("True")'''

#not condition
'''a=5
b=10
if not a>b :
    print("True")'''

'''a=5
b=10
if not a<b and b>a:
    print("True")'''

'''a=2
b=4
if not a<b or b>a:
    print("True")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("True")'''

'''a=4
b=9
if  not a<b or a!=b:
    print("True")'''

#if - condition by using Identify operator
#is,is not
'''a=2
if type(a) is int:
    print("it is int")'''

'''a=2
if type(a) is not int:
    print("it is int")'''

'''a=int(input("Enter the value:"))
if type(a) is int:
    print("true")'''

#using string
'''a="Deekshith"
if type(a) is str:
    print("It is string")'''

'''a=input("Data:")
if type(a) is str:
    print("true")'''

#float
'''a= 7.7
if type(a) is float:
    print("It is float")'''

'''a=float(input("Data:"))
if type(a) is float:
    print("True")'''

#if - condition by using Membership operator
#in, not in
'''a=[10,20,30,40,50]
if 50 in a:
    print("True")'''

'''a=[10,20,30,40,50]
if 30 not in a:
    print("True")'''

'''a=[10,20,30,40,50]
if 60 not in a:
    print("True")'''

'''a=int(input("Enter the value:"))
if 40 in a:
    print("True") '''#error

'''a=[10,20,30,40,50,60]
b=int(input("Enter the value:"))
if b in a:
    print("True") '''


#if-else condition by using comparision
#<,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("True")
else:
    print("False")'''

'''a=2
b=4
if a>b:
    print("True")
else:
    print("False")'''

'''a=int(input("Enter the a  Value"))
b=int(input("Enter the b  Value"))
if a<b:
    print("Less")
else:
    print("True")'''

#if -else condition by using logical operator
#and,or,not
#and
'''a=2
b=4
if a<b and b>a:
    print("True")
else:
    print("False")'''

'''a=2
b=4
if a<b and b<a:
    print("True")
else:
    print("False")'''

#or
'''a=2
b=4
if a<b or b>a:
    print("True")
else:
    print("False")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a>b or b==a:
    print("True")
else:
    print("False")'''



#not
'''a=5
b=10
if not a<b and b>a:
    print("True")
else:
    print("Flase")'''

'''a=int(input("a value"))
b=int(input("b value"))
if  not b==a :
    print("True")
else:
    print("False")'''

'''a=int(input("a value"))
b=int(input("b value"))
if  not a<=b or b==a:
    print("True")
else:
    print("False")'''


#if-else condition by usng Identify operator
#is, is not
'''a=2
if type(a) is int:
    print("True")
else:
    print("False")'''

'''a=int(input("Enter the integer"))
if type(a) is int:
    print("True")
else:
    print("False")'''

#is not
'''a=float(input("Enter the value"))
if type(a) is not float:
    print("True")
else:
    print("False")'''

#if-else - condition by usng Membership operator
#in, not in

'''b=[5,6,7,8,9,10,11]
a=int(input("A value"))
if a in b:
    print("True")
else:
    print("False")'''

'''b=[5,6,7,8,9,10,11]
a=int(input("A value"))
if a not in b:
    print("True")
else:
    print("False")'''

#if-elif-else by using comparasion operators
#<,>,<=,>=,!=,==
'''
a=10
b=20
if a<b:
    print("Less")
elif a>b:
    print("Greater")
else:
    print("True")'''

'''a=10
b=20
if a==b:
    print("Less")
elif a>b:
    print("Greater")
else:
    print("True")'''

'''a=10
b=20
if a==b:
    print("Less")
elif a>b:
    print("Greater")
elif a!=b:
    print("not equal")
else:
    print("True")'''

'''a=10
b=20
if a>=b:
    print("Less")
elif b<=a:
    print("Greater")
elif a!=b:
    print("not equal")
else:
    print("True")'''


#if-elif-else condition by using logical operator
#and,or,not

'''a=10
b=20
if a==b and a<b:
    print("Less")
elif a!=b or a>=b:
    print("Greater")
else:
    print("True")'''

'''a=10
b=20
if a==b and a<b:
    print("Less")
elif a>=b or a==b:
    print("Greater")
elif not a==b:
    print("True")
else:
    print("Flase")'''

#if-elif- condition by using Identify operator
#is, is not

'''a="Nani"
if type(a) is int:
    print("True")
elif type(a) is not int:
    print("False")
else:
    print("Wrong")'''

#if-elif-else  condition by using Membership operator
#in, not in

'''a=[10,20,30,40,50]
if 60 in a:
    print("True")
elif 60 not in a:
    print("Flase")
else:
    print("60 is not Present list")'''

#Multiple if using comparison condition
#<,>,<=,>=,!=,==

'''a=3
b=5
if a<b:
    print("Less")
if b>a:
    print("Greater")
    '''

'''a=7
b=10
if a==b:
    print("Less")
if b>a:
    print("Greater")
if a!=b:
    print("True")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("Less")
if b<a:
    print("Greater")
if a!=b:
    print("True")'''

#Multiple-if condition by using logical operator
#and,or,not

'''a=10
b=20
if a!=b and a<b:
    print("True")
if a!=b or a>=b:
    print("False")
if not a==b:
    print("Less")'''

#Multipl-if condition by using Identify operator
#is, is not

'''a=20
if type(a) is int:
    print("True")
if type(a) is not int:
    print("False")'''

#multiple-if condition by using Membership operator
#in, not in

'''a=[10,20,30,40,50]
if 60 in a:
    print("True")
if 60 not in a:
    print("Flase")'''

'''a=[10,20,30,40,50]
b=input("Enter the a value:")
if b in a:
    print("True")
if b not in a:
    print("Flase")'''

#nested-if Statement
'''a=6
b=8
if a<b:
    print("Less")
    if a!=b:
        print("not eqal")'''

'''a=6
b=8
if a==b:  #statement false so output is empty
    print("Less")
    if a!=b:
        print("not eqal")'''

'''a=12
b=20
if a<b:
    print("Less")
    if a==b:
        print("not eqal")'''

'''a=6
b=8
if a<b:
    print("Less")
    if a!=b:
        print("not eqal")
    else:
        print("True")'''

'''a=10
b=20
if a<b:
    print("Less")
    if a==b:
        print("not eqal")
    elif b<a:
        print("Greater")
    else:
        print("True")'''

'''a=6
b=8
if a>b:
    print("Less")
    if a!=b:
        print("not eqal")
else:
    print("True")'''

a=6
b=8
if a==b:
    print("Less")
    if a>b:
        print("not eqal")
    else:
        print("True")
else:
    print("False")



    










    


    
















    

    
      



    
      
       
