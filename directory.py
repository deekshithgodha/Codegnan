#Directory
#Collecton of files is called the Directory

#print(dr())
#print(dir("--builtins--"))
#fromkeys()

'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

#sting  is not take the dictionary values so we used the Directory
#print(dict(a))

b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"Nani")
print(c)

c["g"]= "Deekshith"
print(c)'''


#eval()
#In eval() used for the possible for all the data 
'''while True:
    a=int(input("a value "))
    b=int(input("b value "))
    print(a+b)

while True:
    a=float(input("a value "))
    b=float(input("b value "))
    print(a+b)'''

#Thee eval() is satisfied the all the data types but in run time we keep the ' ' with input  ex:- Enter the value: 'nani' . like this
'''while True:
    a=eval(input("a value "))
    b=eval(input("b value "))
    print(a+b)'''

#zip() -> We can combine multiple collections into one collection
'''a=[10,20,30,40,50]
names=["Surendar", "harsha", "rupesh","krishna","mohan"]
print(a+names)

#It will not show the output
b=zip(a,names)
print(b)

#In the Zip() we use the  datatype must like below  Using list
c=list(zip(a,names))
print(c)

#Using tuple
c=tuple(zip(a,names))
print(c)

#Dictionary
c=dict(zip(a,names))
print(c)'''


#enumerate()   --> We can give counter to the collection................Don't keep the len in range directly
'''names=["Nani","Buddi", "Guru","Vignesh","Chandra"]
#We dont use the for loop
for i in range(len(names)):
    print(i,names[i])
#with out for loop we can use the enumerate

b=list(enumerate(names))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)'''


#---------Task----------------
while True:
    weight=float(input("Enter the weight:"))
    height=float(input("Enter the height:"))
    bmi= weight / height **2
    if  bmi<=18.5:
        print("Under weight")
    elif bmi > 18.5 and bmi<=24.5:
        print("Normal Weight")
    elif bmi  > 24.5 and bmi<=29.5:
        print("Over Weight")
    else:
        print("Obesity")




    

