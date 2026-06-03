Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

a={3,5.6,"python",6+8j,True,False}
print(a)
{False, True, 3, 5.6, (6+8j), 'python'}

a={5,6,7,8,9,10,11,16,7,8}
print(a)
{5, 6, 7, 8, 9, 10, 11, 16}
a={5,6,7,8,9}
a.add(10)
a
{5, 6, 7, 8, 9, 10}
#issubset()
a={1,2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False
a={4,5,6,7,8,9,10}
b={8,9,10}
a.issuperset(b)
True
b.issuperset(a)
False

#union()
a={5,6,7,8,9,10}
b={8,9,10,11,12,13}
a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12, 13}

#intersection()
a={5,6,7,8,9,10,11,12}
b={1,2,3,4,5,6,7,8,9,10,11}
a.intersection(a)
{5, 6, 7, 8, 9, 10, 11, 12}
b.intersection(a)
{5, 6, 7, 8, 9, 10, 11}

#update()
a={5,6,7,8,9,10}
b={8,9,10,11,12}
a.update(b)
a
{5, 6, 7, 8, 9, 10, 11, 12}
b
{8, 9, 10, 11, 12}
b.update(a)
b
{5, 6, 7, 8, 9, 10, 11, 12}

#diffrence()
a={1,2,3,4,5}
b={4,5,6,7,8}
a.difference(b)
{1, 2, 3}
b.difference(a)
{8, 6, 7}

#symentric_difference()
#its remove the same values from the set and print the remning set
a={3,4,5,6,7,8}
b={6,7,8,9,10}
a.symentric_difference(b)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.symentric_difference(b)
AttributeError: 'set' object has no attribute 'symentric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(a)
set()
a.symmentric_difference(b)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.symmentric_difference(b)
AttributeError: 'set' object has no attribute 'symmentric_difference'. Did you mean: 'symmetric_difference'?
a.symmetric_difference(b)
{3, 4, 5, 9, 10}

#difference_update()
a={5,6,7,8,9,10}
b={8,9,10,11,12}
a.difference_update(b)
a
{5, 6, 7}
b.difference_update(a)
b
{8, 9, 10, 11, 12}

#intersection_update()
a={4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.intersection_update(b)
a
{4, 5, 6}
#when i call the a its shows the updates value only
a
{4, 5, 6}
b
{1, 2, 3, 4, 5, 6}
b.intersection_update(a)
b
{4, 5, 6}

#symmentric_diffrence_update(b)
a={3,4,5,6,7,8}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8}
a
{1, 2, 7, 8}
b.symmetric_difference_update(a)

b
{3, 4, 5, 6, 7, 8}

#copy()
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
a.clear()
a
set()
b=set()
b.add(7)
b
{7}
#Its not possible to insert the multiple values at a time in the sets
a.add(7,8)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.add(7,8)
TypeError: set.add() takes exactly one argument (2 given)

#pop()
a={7,8,9,10,11}
a.pop()
7
>>> a.pop(8)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.pop(8)
TypeError: set.pop() takes no arguments (1 given)
>>> #directly we can not remove the values from the set
>>> #remove the perticular element to remove use remove()
>>> a.remove(10)
>>> a
{8, 9, 11}
>>> 
>>> #discard()
>>> a={1,2,3,4,5}
>>> a.discard(4)
>>> a
{1, 2, 3, 5}
>>> 
>>> b={4,5,6,7,8}
>>> c={1,2,3,4}
>>> b.discard(c)
>>> b
{4, 5, 6, 7, 8}
>>> c
{1, 2, 3, 4}
>>> #dont use the  keep the varible in the
>>> 
>>> #length() = len()
>>> a={1,2,3,4,5,6}
>>> len(a)
6
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> 
#isdisjoint()
a={1,2,3,4,5}
b={4,5,6,7,8}
a.isdisjoint(b)
False
a={1,2,3,4,5}
b={6,7,8,9,0}
a.isdisjoint(b)
True
