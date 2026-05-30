Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Bitwise
a=5
b=3
a&b
1
a=3
b=4
a&b
0
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(5)
'0b101'
>>> bin(3)
'0b11'
>>> bin(7)
'0b111'
>>> bin(2)
'0b10'
>>> bin(8)
'0b1000'
>>> bin(9)
'0b1001'
>>> #|
>>> A=3
>>> B=4
>>> A|B
7
>>> #~
>>> a=2
>>> b=3
>>> a~2
SyntaxError: invalid syntax
>>> a~b
SyntaxError: invalid syntax
>>> a=6
>>> ~a
-7
>>> a=5
>>> b=3
>>> a^b
6
>>> a<<b
40
>>> a>>b
0
