Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthematic
a=2
b=7
print(a+b)
9
print(a-b)
-5
print(a*b)
14
print(a//b)
0
print(a/b)
0.2857142857142857
print(a**b)
128
print(a%b)
2
#Assignment
a=4
b=8
b+=a
b+=8
b+=b
b
40
b-=a
b
36
b*=a
b
144
b//=a
b
36
b/=a
b
9.0
b**/=a
SyntaxError: invalid syntax
b/=a
b
2.25
b**=a
b
25.62890625
b%=a
b
1.62890625
#Comparison
a=4
b=10
a<b
True
b>a
True
a<=b
True
a>=b
False
a==b
False
b==a
False
a!=b
True
b!=a
True
a=7
b=7
a==b
True
#Logical
a=2
b=4
a<b and b>a
True
b>a and a>b
False
a!=b and b!=a
True
>>> a<b and b<a
False
>>> a<b or b<a
True
>>> b>a or b>a
True
>>> b!=a or a==b
True
>>> not True
False
>>> not False
True
>>> #Identify
>>> a=7
>>> if type(a) is int:
...     print("It is int")
... 
...     
It is int
>>> if type(a) is not int:
...     print("True")
... 
...     
>>> #Membership
...     
>>> a= 1,2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print("The number is there")
... 
...     
The number is there
>>> if 20 in a:
...     print("Flase")
... 
...     
>>> if 20 not in a:
...     print("The number is not there")
... 
...     
The number is not there
