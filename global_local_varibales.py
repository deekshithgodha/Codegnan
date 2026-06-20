#Global and Local Variable
#Variable inside and output function is clalled Global and local variable
#a Variable define above the function and is access to the entire global space is called global varibale
#a Variable is defines inside the function is called the Local function

#first case of global variable
'''a=3
def check():
    print("inside the value is",a)
check()
print("outside value is",a)'''

#second case of global varibale
'''a=2
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("Outside value is",a)'''

#Third case of both global and local variable
'''a=4
b=9
def check2():
    a=3
    print("Inside the value is",a)
    a=10
    print("Updated  values is",a+5)
    b=12 #local varibes
    b=b+a
    print("Values of b is", b)
check2()
print("a value is",a)
print(" b value is",b)

#Error
a=4
def check2():
    a=3
    print("Inside the value is",a)
    a=10
    print("Updated  values is",a+5)
    b=12 #local varibes
    b=b+a
    print("Values of b is", b)
check2()
print("a value is",a)
print(" b value is",b)'''


#Usage of global key word
#When user whats to access the global varibale inside the functon directly and carry forward the updated value even outside the function then we use the global key word
#Final case of  both global and local variables
a=4
def final():
    global a,b
    print("Inside value is",a)
    a=5
    print("Updated value is",a)
    #global b
    b=13
    b=b+a
    print("b value is",b)
final()
print("value of a is",a)
print("value of b is",b)


