Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatypes
a=5
type(a)
<class 'int'>
b=6.9
type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="Gnan"
>>> type(d)
<class 'str'>
>>> e="Deekshith"
>>> type(e)
<class 'str'>
>>> f='''Nani'''
>>> type(f)
<class 'str'>
>>> f=5+2j
>>> type(f)
<class 'complex'>
>>> g=6j-2
>>> type(g)
<class 'complex'>
>>> k=j
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    k=j
NameError: name 'j' is not defined
>>> k=1j
>>> type(k)
<class 'complex'>
>>> z=True
>>> type(z)
<class 'bool'>
>>> y=False
>>> print(y)
False
>>> x=|"True"
SyntaxError: invalid syntax
>>> x="True"
>>> print(x)
True
>>> type(x)
<class 'str'>
