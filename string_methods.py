Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #String Methos
>>> #len
>>> a="Deekshith Naga Prasanna"
>>> len(a)
23
>>> b="Raghu Vamshi"
>>> len(b)
12
>>> c="Hastalavista_"
>>> len(c)
13
>>> d=""
>>> len(d)
0
>>> #Count
>>> a="Johy Jony Yes Papa"
>>> a.count("Papa")
1
>>> a.count("P")
1
>>> a.count("a")
2
>>> a.count(" ")
3
>>> #Find a string
>>> a="Pyhon"
>>> a.find("h")
2
>>> a.find("P")
0
>>> b="Deekshith"
>>> a.find("h")
2
>>> b.find("h")
5
>>> a.find("z")
-1
>>> #escape Sequences
>>> #\n --> New line
#\t--> Tab Space
a="name\nnameid\tmobileno"
print(a)
name
nameid	mobileno
b="name:Pooja\nmailid:godhadeekshith799@gmail.com\tmobileno:8096142793"
print(b)
name:Pooja
mailid:godhadeekshith799@gmail.com	mobileno:8096142793
c="name:Deekshith\nmailid:nani@gmail.com\tmobileno:9087627172"
print(c)
name:Deekshith
mailid:nani@gmail.com	mobileno:9087627172
#replace()
a="Wait until you succeed"
a.replace("Wait","Work")
'Work until you succeed'
b.replace("Wait","Work",1)
'name:Pooja\nmailid:godhadeekshith799@gmail.com\tmobileno:8096142793'
a.replace("Wait","Work",1)
'Work until you succeed'
b="wait wait until you succed"
b.replace("wait","work",1)
'work wait until you succed'
#UPPER()
a="deekshith"
a.upper()
'DEEKSHITH'
#lower
b="CODEGNAN"
b.lower()
'codegnan'
c="nani"
#Title()
a="iam a good boy"
a.title()
'Iam A Good Boy'
b="chandra is topper"
a.title()
'Iam A Good Boy'
b.title()
'Chandra Is Topper'
#Capitalize()
a="deekshith"
capitalize()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    capitalize()
NameError: name 'capitalize' is not defined
a.capitalize()
'Deekshith'
#Conditions on These methos
a="hello"
a.isupper()
False
a.islower()
True
a.title()
'Hello'
a.istitle()
False
a.isalpha()
True
b="Hello World")
SyntaxError: unmatched ')'
b="Hello Wipro"
a.isalpha()
True
e=1234
a.isdigit()
False
l="1234"
l.isdigit()
True
#Alpha numaric
a="deekshith123"
a.isalnum()
True
b="java"
a.isalnum()
True
k="deekshith@123"
k.isalnum()
False


c="java"
c.startswith(|"j")
SyntaxError: invalid syntax
c,startswith("j")
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    c,startswith("j")
NameError: name 'startswith' is not defined
s="java"
s.startswith("j")
True

#Strip()
#lstrip(), rstrip()
a="     Nani         "
strip()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    strip()
NameError: name 'strip' is not defined
a.strip()
'Nani'
a.lstrip()
'Nani         '
a.rstrip()
'     Nani'


#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="pythonjava"
b.split()
['pythonjava']
d="ml       ds"
d.split()
['ml', 'ds']
