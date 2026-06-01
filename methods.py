Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #join()
>>> a="python","java","c"
>>> "".join(a)
'pythonjavac'
>>> " ".join(a)
'python java c'
>>> #formatting
>>> #Adding the additional data
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> print("The sum is",a+b)
The sum is 30
>>> print("The sum is,a+b")
The sum is,a+b
>>> 
>>> #Concatenation
>>> a="pyhton"
>>> b="course"
>>> print(a+b)
pyhtoncourse
>>> print(a+" "+b)
pyhton course
>>> fname="Deekshith"
>>> lname="Goda"
>>> print(fname+lname)
DeekshithGoda
>>> print(fname+" "+lname)
Deekshith Goda
>>> print(fname.title()+" "+lname.title())
Deekshith Goda
>>> print((fname+" "+lname).title())
Deekshith Goda
>>> 
>>> #Formating method
>>> #adding the number of additional strings
>>> a="motu"
>>> b="patlu"
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu

#fstring
a="micky"
b="mouse"
print(f"hello {a} {b}")
hello micky mouse
print(f"hello {a} hello{b}")
hello micky hellomouse

#Indexing
#1.Positive Index
#2.Negative Index
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[11]
'class'
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[5]+a[6]
'in'
a[2]+a[3]
'am'
a[1]+a[4]+a[7]
'   '
#2. Negative Index
1.#positive index
1.0
#positive index
a="vijayawada"
a[3]
'a'
a[5]+a[4]
'ay'


#1.Positive index
a="vijayawada is a royal city"
a[17]+a[18]+a[19]+a[20]+a[21]
'oyal '
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'

b="vizag is a city of destiny"
b[11]+b[12]+b[13]+b[14]
'city'
b[19]+b[20]+b[21]+b[22]+b[23]+b[24]+b[25]
'destiny'
b[0]+b[1]+b[2]+b[3]+b[4]
'vizag'

#again Negative
a="i am in python class"
a[-12]+b[-11]+b[-10]+b[-9]+b[-8]+b[-7]
'p of d'
a[-12]+a[-11]+a[-10]+a[-9]+a[-8]+a[-7]
'python'
a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'class'
a[-18]+a[-17]
'am'

b="simple is better than complex"
b[-7]+b[-6]+b[-5]+b[4]+b[-3]+b[-2]
'comlle'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+a[-1]
'comples'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'complex'
b[-19]+b[-18]+b[-17]+b[-16]+b[-15]+b[-14]
'better'
b[-29]+b[-28]+b[-27]+b[-26]+b[-25]+b[-24]
'simple'

#Slicing
#1.Positive Sclicing
#Sorry its Slicing
#Negative Slicing

#Positive
a="Work until you succed"
a[50:11]
''
a[5:11]
'until '
a[5]
'u'
a[:5]
'Work '
a[11:15]
'you '
a[15:]
'succed'
a[:15]
'Work until you '
b ="Codegnan it solutions"
a[9:12]
'l y'
b[9:12]
'it '
b[4:9]
'gnan '
a[12:20]
'ou succe'
b[12:20]
'solution'

#Negative Slicing
a="i am learning python"
a[-15:-10]
'learn'
a[-7:]
' python'
