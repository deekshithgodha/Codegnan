Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Striding
a="data Science"
a[::]
'data Science'
a[::1]
'data Science'
a[::2]
'dt cec'
b="Cloud Computing"
a[::4]
'd e'
b=[::4]
SyntaxError: invalid syntax
b=[::4]
SyntaxError: invalid syntax
a[::4]
'd e'
a="cloud computing"
a[::4]
'cdmi'
>>> a[::3]
'cucpi'
>>> a[::6]
'cci'
>>> a[3:6]
'ud '
>>> a[:9]
'cloud com'
>>> a[7:]
'omputing'
>>> a="machine learning"
>>> a[2:14:4]
'cea'
>>> a[3:15:5]
'hli'
>>> a[1:2:5]
'a'
>>> a[1:12:2]
'ahn er'
>>> #Negative Striding
>>> a="python course"
>>> a[-1:-11:-14]
'e'
>>> a[-1:-11:-4]
'eoo'
>>> a[-3:-12:-5]
'rn'
>>> a[-5:-12:-6]
'ot'
>>> a[-2:-9:-11]
's'
>>> a[-2:-9:-1]
'sruoc n'
>>> a[-6:-13:-3]
'coy'
>>> a[-3:-12:-6]
'ro'
>>> a[-4:-12:-6]
'uh'
