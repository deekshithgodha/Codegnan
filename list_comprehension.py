#List Comprehension

'''a=["python","codegnan","Course"]
#print(a.upper())

b=str(a)
print(b.upper(),end="")

a=["python","codegnan","Course"]
b=[i.upper() for i in a]
print(b)

a=["vja","hyd","viz"]
b=[i.capitalize() for i in a]
print(b)

a=["PYTHON","CODEGNAN","COURSE"]
b=[i.lower() for i in a]
print(b)

a=[2,3,4,5,6,8,12,13]
#b=[i**2  for i in a]
#b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)

#Using Range
num=int(input("Enter the value"))
range_=[d for d in range(num)]
print(range_)

while True:
num=int(input("Enter the number"))
a=[c for c in range(21) if c%2==0]
print(a)

a=[c*c for c in range(21) if c%2==0]
print(a)

fruits=["apples","banana","grapes","kiwi","mango","berry"]
a=[i for i in fruits if "a" in i]
print(a)

fruits=["apples","banana","grapes","kiwi","mango","berry"]
a=[i for i in fruits if "a" not in i]
print(a)

#no-elif usage in list - comprehension
num=int(input("Enter the number"))
a=[i*i if i%2==0 else i*5 for i in range(num) ]
print(a)

a=[1,2,3,4,5]
b=[5,4,3,2,1]
add=[a[i]+b[i] for i in range(5)]

#add=[a[i]+b[i] for i in range (len(a)) ]
print(add)'''


#---------------------------------------ATM APPLICATON-------------------------------------
while True:
    balance=100000
    card=input("Insert the card")
    if  card=="c":
        print("Welcome Deekshith")
        password=int(input("Enter the password"))
        if password==1234:
            print("\nOptions:")
            print("1.Balance enquiry")
            print("2.With draw ")
            option=int(input("Enter option:"))
            if option ==1:
                print("Available Balance =", balance)
            elif option==2:
                amount=int(input("Enter withdeaw amount:"))
                if amount <=balance:
                    balance=balance - amount
                    print("Please collet the money")
                    print("Debited Amount =",amount)
                    print("Remaining Balence=", balance)
                else:
                    print("Insufficient Balence")
            else:
                print("Invalid Option")
        else:
            print("Wrong Password")
    else:
        print("Please Insert Valid Card")
                    
            
            
            
            








