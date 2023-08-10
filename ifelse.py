#array in python
a=int(input("enter the value of A "))
b=int(input("enter the value of B"))
c=int(input("enter the value of C"))
d=int(input("enter the value od D"))
if(a>b):
    if(a>c):
        if(a>d): 
            print("a is greater")
        else:
            print("d is greater")
    else:
        print("c is greater")
elif(b>c):
    if(b>d):
        if(b>a):
             print("b is greater")
        else:
             print("a is greater")
    else:
        print("b is greater")  
elif(c>d):
    if(c>a):
        if(c>b):
            print("c is greater")
        else:
            print("b is greater")
    else:
        print("a is greater")
else:
    if(d>a):
        if(d>b):
            print("d is gretaer")
        else:
            print("b is greater")
    else:
        print("a is greater")