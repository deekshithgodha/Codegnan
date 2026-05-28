Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 #variables
print(7+9)
16
x=100
print(x)
100
Z=100
print(Z)
100
#dont start with number
5=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
7=10
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#start with alphabet
a7=100
print(a7)
100
20a=100
SyntaxError: invalid decimal literal
a01234567=30
print(a01234567)
30
#start with names
name="nani"
print(name)
nani
place="vij"
print(place)
vij
country="india"
print(country)
india
#dont start with special characters
@=9
SyntaxError: invalid syntax
&=0
SyntaxError: invalid syntax
#but start with underscore
_0=100
print(_0)
100
#its not take the spaces also
 x=90
 
SyntaxError: unexpected indent
_=100
print(_)
100
#dont start with keywords
if=30
SyntaxError: invalid syntax
else=90
SyntaxError: invalid syntax
#In single lines takes multple values
a=3,b=8
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=8
print(a+b)
11
a,b=5,6
print(a+b)
11
a=1,2,3,4,5,6
print(a)
(1, 2, 3, 4, 5, 6)
#single variable to multiple values
#single variable to multiple values
#multiple varible to single value
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=20
print(ab,c)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(ab,c)
NameError: name 'ab' is not defined. Did you mean: 'a7'?
>>> print(a,b,c)
20 20 20
>>> #dont give the spaces b/w varibales
>>> first name="Nani"
SyntaxError: invalid syntax
>>> first_name="Nani"
>>> print(first_name)
Nani
>>> firstname="Nani"
>>> print(firstname)
Nani
>>> fame="Nani"
>>> lname="G"
>>> print(fame+lname)
NaniG
>>> print(fame+" "+lname)
Nani G
>>> #unpacking and deleting
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> x=10
>>> print(x)
10
>>> dlt x
SyntaxError: invalid syntax
>>> del x
>>> #case sensitive
>>> Age=10
>>> print(Age)
10
>>> age=20
>>> print(age)
20
>>> AGE=30
>>> print(AGE)
30
