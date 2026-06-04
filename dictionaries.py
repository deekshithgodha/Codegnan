Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dictionaries
a={"name":"Deekshith","year":2003,"month":"August"}
print(a)
{'name': 'Deekshith', 'year': 2003, 'month': 'August'}
type(a)
<class 'dict'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.items()
dict_items([('name', 'Deekshith'), ('year', 2003), ('month', 'August')])
a.values()
dict_values(['Deekshith', 2003, 'August'])

 
#adding the data
a={"city":"vij","country":"india"}
a.update({"state":"NTR"})
a
{'city': 'vij', 'country': 'india', 'state': 'NTR'}
a.update({"city":"ap","district":"kadapa"})
a
{'city': 'ap', 'country': 'india', 'state': 'NTR', 'district': 'kadapa'}
#Dont pass the multiple values in the update
a.update({"city":"anathapur"}{"district":"rayalaseema"})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a.update{"city":"anathapur"}{"district":"rayalaseema"}
SyntaxError: invalid syntax
a.update({"city":"anathapur"}),({"district":"rayalaseema"})
(None, {'district': 'rayalaseema'})

#Set_Default()
a={"day":"Monday","date":7}
a.setdefault("time",8)
8
a
{'day': 'Monday', 'date': 7, 'time': 8}

#get()
a={"name":"Deekshith","mailid":"nani@gmail.com"}
a.get("name")
'Deekshith'
a["name"]
'Deekshith'
a["Deekshith"]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a["Deekshith"]
KeyError: 'Deekshith'
a.get("Deekshith")
a
{'name': 'Deekshith', 'mailid': 'nani@gmail.com'}

#pop()
a={"city":"Viz","mobile_no":73836272723,"mail_id":"nani@gamil.com"}
a
{'city': 'Viz', 'mobile_no': 73836272723, 'mail_id': 'nani@gamil.com'}
a.pop()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0

#we passed the value what we want to pop
a.pop("city")
'Viz'
a.popitem()
('mail_id', 'nani@gamil.com')
a
{'mobile_no': 73836272723}

#Copy()
a={"data":4,"month":6,"time":10}
a.copy()
{'data': 4, 'month': 6, 'time': 10}
a
{'data': 4, 'month': 6, 'time': 10}

#clear()
a.clear()
a
{}

>>> #len()
>>> a={"data":4,"month":6,"time":10}
>>> len(a)
3
>>> 
>>> a={"name":"deekshith","city":"Viz","name":"Deekshith"}
>>> print(a)
{'name': 'Deekshith', 'city': 'Viz'}
>>> a={"name":"deekshith","city":"Viz","name":"deekshith"}
>>> a
{'name': 'deekshith', 'city': 'Viz'}
>>> a={"name":"Deekshith","city":"Viz","name1":"Nani"}
>>> a
{'name': 'Deekshith', 'city': 'Viz', 'name1': 'Nani'}
>>> 
>>> #index()
>>> a={"name":"deekshith","city":"Viz","name":"Deekshith"}
>>> a.index("name")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.index("name")
AttributeError: 'dict' object has no attribute 'index'
>>> #count()
>>>  a={"name":"deekshith","city":"Viz","name2":"Deekshith"}
...  
SyntaxError: unexpected indent
>>> a={"name":"deekshith","city":"Viz","name2":"Deekshith"}
>>> a
{'name': 'deekshith', 'city': 'Viz', 'name2': 'Deekshith'}
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
>>> a={"idnos":[10,20,30],"names":["Bhanu","Deekshith","Adil"],"marks":[89,10,40]}
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['Bhanu', 'Deekshith', 'Adil'], [89, 10, 40]])
