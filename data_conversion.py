Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes conversions
#int
int(8)
8
int(7.7)
7
int("Deekshith")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Deekshith")
ValueError: invalid literal for int() with base 10: 'Deekshith'
int(6+7j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(Flase)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
int(False)
0
#String
str(7)
'7'
str("Nani")
'Nani'
str(7.7)
'7.7'
str(True)
'True'
str(False)
'False'
#float
float(7)
7.0
float("Nani")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float("Nani")
ValueError: could not convert string to float: 'Nani'
float(7.7)
7.7
>>> float(True)
1.0
>>> float(False)
0.0
>>> #complex
>>> complex(7)
(7+0j)
>>> complex("Nani")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex("Nani")
ValueError: complex() arg is a malformed string
>>> complex(7.7)
(7.7+0j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #Bool
>>> bool(8)
True
>>> bool("Deekshith")
True
>>> bool(7.7)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(9+7j)
True
>>> complex(7+6j)
(7+6j)
>>> float(7+8j)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float(7+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(7+0j)
'(7+0j)'
