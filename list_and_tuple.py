Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List[]
#List is mutable
a=[3, 5.6, "python", 8+9j+True, False]
print(a)
[3, 5.6, 'python', (9+9j), False]
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>

#Methods in Lits[]
#append()
a=["python","java","c"]
a.append("ml")
a
['python', 'java', 'c', 'ml']

#in append method take only 1 value
a.append("c++","sql")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append("c++","sql")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c++","sql"])
a
['python', 'java', 'c', 'ml', ['c++', 'sql']]

#extend()
a=["apple","banana"]
a.extend(["mango","grapes"])
a
['apple', 'banana', 'mango', 'grapes']

#insert()
a=["black","white","red"]
a.insert(1,"pink")
a
['black', 'pink', 'white', 'red']

#index()
a=["ml","ai","ds"]
a.index("ds")
2

#copy()
a.copy()
['ml', 'ai', 'ds']
b=a.copy()
b
['ml', 'ai', 'ds']

#sort()
a=["yellow","green","red"]
a.sort()
a
['green', 'red', 'yellow']
b=[8,3,6,1,4,0,5,7]
a.sort()
a
['green', 'red', 'yellow']
b.sort()
b
[0, 1, 3, 4, 5, 6, 7, 8]
#reverse()
a=["Vij","hyd","viz"]
a.reverse()
a
['viz', 'hyd', 'Vij']
b=[1,8,6,3,,8,9,5]
SyntaxError: invalid syntax
b[1,2,3,4,5,6,7,8,9]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b[1,2,3,4,5,6,7,8,9]
TypeError: list indices must be integers or slices, not tuple
b=[1,2,3,4,5,6,7,8,9]
b.reverse()
b
[9, 8, 7, 6, 5, 4, 3, 2, 1]

#pop()
a=["python","java","c"]
a.pop()
'c'
a.pop(1)
'java'
a
['python']
#Dont write string name in pop() inside function
a.pop("python")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.pop("python")
TypeError: 'str' object cannot be interpreted as an integer

#remove()
a.remove("python")
a
[]

#length & count
a=["hi","hello","hoe"]
>>> len(a)
3
>>> b="hello"
>>> len(b)
5
>>> 
>>> #clear()
>>> a=["python","java"]
>>> a.clear()
>>> a
[]
>>> b.append("Deekshith")
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    b.append("Deekshith")
AttributeError: 'str' object has no attribute 'append'
>>> b=[]
>>> b.append("Deekshith")
>>> b
['Deekshith']
>>> 
>>> #TUPLE()
>>> a=(5, 6.7, "python", 8+9j+,True, False)
SyntaxError: invalid syntax
>>> a=(5, 6.7, "python", 8+9j,True, False)
>>> print(a)
(5, 6.7, 'python', (8+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> 
>>> #length()
>>> len(a)
6
>>> 
>>> #count()
>>> a.count(True)
1
>>> #index()
>>> a.index("python",)
2
