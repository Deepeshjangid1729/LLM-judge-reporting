#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("ram ")


# In[2]:


print(f"""name deepesh jangid
      address jaipur 
      course ml
      degree b.tech""")


# In[4]:


''' this 
 is deepesh jangid '''
print("deepesh jangid")


# In[5]:


#deeepesh jangid
print("ram")


# In[8]:


fname="deepesh"
print(fname,id(fname))
c="tushar"
print(c,id(c))
d="deepesh"
print(d,id(d))


# In[9]:


fname="mukul"
print(fname,id(fname))


# In[13]:


fname="this is my collage "
fname[-1:-10:-1]


# In[14]:


print("this is deepesh jangid ")


# In[15]:


def square(a):
    sq=a*a
    return sq
square(5)
    


# In[20]:


i=1
for i in range(1,10):
    print("jai shree ram")
    


# In[21]:


for i in range(1,5):"


# In[22]:


for i in range(1,5):
    print("jao re ")


# In[23]:


def factorial(value):


# In[28]:


def factorial(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i
        return fact
    n=10
    r=3
    c= factorial(n)/(factorial(r)*factorial(n-r))
    print(+str(c))
    


# In[31]:


def fun(n,l=[]):
    for i in range(n):
    l.append(i*i)
    print(l)
    
fun(2)
    


# In[ ]:


i=1
while True:
    if i%9==0:
        break
        print(i+4)
        i+=2


# In[ ]:


string="intershala"
fir i in range(len(string)):
    print(string)
    string='d'
    print(string)


# In[ ]:


Raw_Housing_Data.dtypes


# In[1]:


import keyword


# In[3]:


a = 3-4-5\
    4-4-4
a


# In[4]:


a,v,b=12,34,55
a


# In[5]:


5+6*3**2


# In[6]:


pwd


# In[1]:


state ="bihar"
state[0:2:]


# In[3]:


dir(_buildins_)


# In[4]:


#floor division 
20//3


# In[5]:


#power
2**3


# In[6]:


#modulas 
10%3


# In[8]:


10+2-5*2/2+5-1


# In[9]:


2**3**2
#start at right side


# In[11]:


#camparion  opertor =>
x=9  #assigment opertor
x==9 # camprion
# , . <=>=


# In[12]:


#assigment opertor
''' uniary  x++ ,y++   binaery '''
x=5
x=x+5  
x+=5
print(x)


# In[13]:


x=2
x**=4
x=x**4
print(x)


# In[15]:


x**4
print(x)


# In[20]:


#logical operator and, or, not, &&, ||, !,
x=10
x==10
y=15
#if both condition are true then give the ture otherwise false

#x==19 and y==21
x==12 or y==12


# In[22]:


# bit wise bit pr kam krege 
'''8421
11 1011
10 1010
---------
|  1011
&  1010


2-->128 64 32 16


'''

11 &10
11 |10


# In[24]:


#bitwise lift shift or right shift 
'''
formula number//2**bit  -->bitwise right shift
13//2**1=13//2=6
44//2*2=44//4=11

number*(2**bit)

'''
44>>2


# In[ ]:


'''
**
* / // %
+ - (same left to right)

1/08/2023
assigment-->


bitwise xor opertor 
namespace in python
compiler vs interpretor vs encoder
 
'''


# In[2]:


#bitwise xor opertor
a=5 
b=3
c=a^b
print(c)


# In[26]:


'''
membership =>pata krne ke liye  member dusre data ke andar

in  and not in 
case senstive hoti hai


'''
"t"not in "tushar"


# In[27]:


'''
identitiy opeertaor
type of data
is and is not 

'''
x=10
type(x)is int 


# In[36]:


# conditional statemnent 
x=12
if(x==1):
       print("true")
   
elif(x==13) :
       print("fulse")
else :        
       print("kj3r3")


# In[43]:


x=12
y=2
if(int==type(x) and int==type(y)):
    print("arthematic  opertion allow")
else:
    print("not allow")
     


# In[44]:


x=input

'''


# In[ ]:


'''
1 three input user and identify the small number 
2  take a string user take a another string check a small string is avallable in large string
3  take a char identify vowal or not 
4  take a input user perfore the task
1  user take input 1 print curreent date 
  user take 2 input to ham destop per folder bnanan hai 
    user input 3 desktop per jo bi file hai sab dekni hai 
    user 4 input to muje whatups per message send krna h
    ''''


# In[1]:


import datetime
current_date= datetime.date.time()
a=input("press the one for current date")
if(a!=1):
    print("current date",current_date)
else:
    print("not")


# In[ ]:


a=input("enter the value of :")
b=input("enter the value b:")
c=input("enter the value of c :")
print("check the small number")
if(a<b and a<c):
    print("a is small ",a)
elif(b<a and b<c):
    print("b is small",b)
else:
    print("c is small",c)
    


# In[1]:


a=input("enter the value of :")
b=input("enter the value b:")
c=input("enter the value of c :")
print("check the small number")
if(a<b and a<c):
    print("a is small ",a)
elif(b<a and b<c):
    print("b is small",b)
else:
    print("c is small",c)
    


# In[3]:


str1=input("enter is large string")
str2=input("enter the small string")
if(str2 in str1):
    print("avilable in string1")
else:    
    print("not available")


# In[ ]:


x=input("enter the charactor :")
print("check the letter is vowal or not ")
if(x=="a"or x=="e"or x=="i" or x=="o"or x=="u"or x=="A"or x=="E"or x=="I"or x=="o" or x=="u"):
    print("letter is vowal")
else:    
    print("not vowal")


# In[4]:


import datetime
current_date=datetime.date.today()
a=input("enter the 1 for date ")
if(a==1):
    print("current date",current_date)
else:
    print("date is not")


# In[1]:


import os
folder_name = input("Enter the folder name: ")


desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')


folder_path = os.path.join(desktop_path, folder_name)


if os.path.exists(folder_path):
    print("Folder with the same name already exists.")
else:
    # Create the folder if it doesn't exist
    os.makedirs(folder_path)
    print(f"Folder '{folder_name}' created successfully on the desktop.")


# In[ ]:


# destop per folder create krna 
import os
folder_name=input("enter the folder name")
desktop_path=os.path.join(os.path.join(os.path.expanduser('~')),'desktop')

folder_path=os.path.join(desktop_path,folder_name)
if


# In[2]:


def send_whatsapp_message(message):
    # In this function, you can implement the code to send the WhatsApp message.
    # Since the actual WhatsApp API is not publicly available, we can't provide the complete implementation here.
    # You may use third-party libraries or services to interact with the WhatsApp API.

    # For the sake of this example, we'll just print the message instead of sending it.
    print("Sending WhatsApp message:", message)


def main():
    # Ask the user to input a number
    num = int(input("Enter a number (4 in this case): "))

    # Check if the number is equal to 4
    if num == 4:
        # Ask the user to input the WhatsApp message
        whatsapp_message = input("Enter the WhatsApp message: ")
        send_whatsapp_message(whatsapp_message)
    else:
        print("The number should be 4 to send a WhatsApp message.")


if __name__ == "__main__":
    main()


# In[3]:


fruits=["apple","banana","cheery","kiwi"]
for fruit in fruits:
    print(fruit)


# In[4]:


print(len(fruits))


# In[5]:


fruits[2]="orange"


# In[6]:


print(fruits)


# In[8]:


counter=0
while counter<=5:
    print(counter)
    counter=counter+1
 


# In[ ]:


#contune and break 
#contune jo value ko 
'''
append jo value ko list me dalti hai 
'''


# In[11]:


num_list=[]
# multiple input 
n=5
for i in range(n):
    num=input("enter the value ")
    num_list.append(num)
    print(num_list)


# In[15]:


num_list=[int(input("enter the value "))for _ in range(5)]
print(num_list)
num_list.sort()


# In[19]:


input_string=input("enter the multiple sppace")
input_list=input_string.split()
number=[int(num) for num in input_list]
number


# In[20]:


#space separate input three and add the print
#sentence input word count in 
#user se list me data lena hai or maxi or mini print krna hai
#list 1 2 3 4 


# In[28]:


input_number=input("enter the three number")
input_list=input_number.split()
number=list(map(int,input_list))
number


# In[29]:


input_number=input("enter the three number")
input_list=input_number.split()



# In[1]:


input_sent=input("enter the sentence")
word=input_sent.split()
count=0
for num in word:
    count=count+1
print(count)   
print(len(word))


# In[4]:


input_list=[input("entert the number")for _ in range(5)]
max_val=max(input_list)
print(max_val)
min_val=min(input_list)
print(min_val)


# In[3]:


input_list=input("enter the ").split()
numbers=[int(num)for num in input_list]
result=[num**2 if i%2==0 else num**3 (for i,num in enumerate(numbers)) ]


# In[1]:


input_list=input("enter the value ").split()
numbers=[int(num) for num in input_list]
result=[num**2 if i%2==0 else num**3 for i,num in enumerate(numbers)]
print(result)


# In[3]:


#list ke word ko ulta krna  
input_list=input("enter the list").split()
string =[str(num) for num in input_list]
result=[word[::-1]for word in string]
print(result)


# In[11]:


input_list=input("enter the list").split()
numbers=[int(num) for num in input_list]
result=[word[::-1] for word in numbers]



# In[20]:


#list ke elemnt ka sum 
input_list=input("enter the value").split()
numbers=[int(num) for num in input_list]
add=0
for i in numbers:
    add=i+add
    
print(add)


# In[25]:


input_list=input("enter the value").split()
numbers=[int(num) for num in input_list]


# In[27]:


numbers=list(range(1,6))
numbers


# In[30]:


age=2
while age<=15:
    print("yoyo")
    age+=1


# In[1]:


lst=[1,2,3,4,5]
for i in lst:
    #if i==3:
    #    break
    if i==4: 
        continue
    print(i)   


# In[4]:


input_string=input("enter the input")
input_list=input_string.split()
numbers=list(map(int,input_list))
numbers


# In[9]:


#list leni hai or new list me prime number print krana hai
input_list=input("enter the list")
input_new =input_list.split()
numbers=list(map(int,input_new))


# In[10]:


for i in range(10):
    print(i)


# In[22]:


for i in range(2,10):
    if(10%i==0):
        print("prime")
    else:   
        print("not prime")


# In[30]:


input_string=input("enter the strig")
b=input_string.split()
word_list=[ word for word in b if word[0]==word[-1] ]
word_list


# In[39]:


input_string=input("enter the strig")
b=input_string.split()
word_list=[word  for word in b if word[::1]==word[::-1]]
word_list


# In[44]:


#append se elment add krn ah 
word_list.append(123)
word_list


# In[45]:


#insert fun insert krta h ek particular jagha per
word_list.insert(2,34)
word_list


# In[46]:


#remove kisi val ko remove krne ke liye kam aata hword_list.
word_list.remove(34)
word_list


# In[49]:


#word_list.pop()
word_list.sort()
word_list


# In[50]:


word_list.append(23)


# In[51]:


word_list.sort()


# In[ ]:


#print 1 to 5 //even number 1 to 10 //sum of even number //multiple by 5 1 to 10//factorial //string input -- check the vowal
#user input number in list  and print avg // 



# In[53]:


#1 to 5
for i in range(1,6):
    print(i)


# In[54]:


#even number
for i in range(1,11):
    if(i%2==0):
        print(i)


# In[56]:


#sum of even number
sum=0
for i in range(1,11):
    if(i%2==0):
        sum=sum+i
print(sum)


# In[58]:


#factorial
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)    


# In[7]:


string=["a","b","c","d","e","i"]
for i in string:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        print("vawal")
    else:
        print("not vawal")


# In[9]:


# avg the list
lst=[1,2,3,4,5]
avg=0
for i in lst:
    avg=avg+i
value=int(avg/len(lst))
print(value)
    
    


# In[16]:


#multiple of 5
num=5
for i in range(1,11):
    multiple=num*i
    print(multiple)


# In[20]:


#prime number
num=int(input("enter the number"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
        else:
            print("prime")
else:
    print("1 se kam h")


# In[11]:


mydict={1:"deep",'sid':'tushar','friend':'deep'}
print(mydict)
#upadate 
mydict[1]="yash"
print(mydict)
mydict[1]


# In[12]:


mydict["email"]="deepesh@hmail.com"
mydict


# In[19]:


mydict.get("email","yash")


# In[21]:


mydict.keys()


# In[22]:


mydict.pop("sid")


# In[24]:


mydict.popitem()#delete last item  
# in tuple 


# In[25]:


mydict.setdefault()


# In[ ]:


#assigment
#update
#setdefaults
#enumerable


# In[28]:


mydict={1:'yash',2:"jaipur",'regex':"deep"}
for data in mydict:
    print(data,mydict[data])


# In[29]:


for data in mydict.values():
    print(data)
    


# In[39]:


mytuple=(10,20)
print(type(mytuple))
x,y=mytuple # tuple unpacking
print(x,y)


# In[38]:





# In[32]:


mydict.items()


# In[35]:


mylist=[(1, 'yash'), (2, 'jaipur'), ('regex', 'deep')]
for i in mylist:
    key,data=i
    print(key,data)


# In[37]:


# Q1 take a input from a user and find the all the consoant with count in from of dictionary
# Q2 read the logic for primary number ,fibnonicc series
# Q3 armstrong ,pallimdrome
# Q4 deep copy and shallow copy


# In[ ]:


#SET
datatyple mutable =>mathematical opertional
it contain the unique elment
set unordered hota hai


# In[41]:


myset=set({})
print(type(myset))


# In[43]:


myset={10,20,30,30,40,(10,20)}
print(myset)


# In[45]:


myset.add(100)
myset


# In[46]:


myset.clear()


# In[47]:


myset.copy()


# In[48]:


myset={10,20,30,30,40,(10,20)}


# In[51]:


myset.remove(50) #remove 


# In[52]:


myset.discard(10)  #remove the data hai to nhi to skip kr dega 


# In[59]:


myset1={1,2,3,4,5}
myset2={2,43,5,6,7}
#myset1.union(myset2)
myset1.intersection_upadate(myset2)


# In[ ]:


#difference ,isdisjoint method ,and issuperset
Q1. take a input user sare unipue word 
1 seq meter nhi krega


# In[1]:


myset={}
for i in myset:
    i=input("enter the word")
    print(i)


# In[24]:


word=input("enter the word").split()
set1=set({word})
set1.word

print(myset)


# In[82]:


for i in range(0,4):
    print(i)
    for j in range(0,4):
        if()
            print("*")
        else:
            print(end="")
print("\n")        


# In[36]:


mylist=[10,20,30]
newlist=[i for i in mylist] #list compressation 
newlist
    


# In[34]:





# In[41]:


invite1={"aman","raj","shyam"}
invite2={"happy","love","aman"}
set1={ x for x in invite1.intersection(invite2)}
print(set1)                                     


# In[56]:


list1=["aman","deep","raj"]
list2=["aman","sunil","raja"]
newlist=[x for x in list1 if x in list2]
print(newlist)


# In[97]:


#fibronic series
num1=0
num2=1
num3=0
for i in range(11):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
    
    
    


# In[13]:


#prime number
num=int(input("enter the number"))
if(num>1):
    for i in range(2,100):
        if(num%i==0):
            print("num is not prime")
            break
        else:
            print("num is prime")
            break

else:
    print("num is not prime")
            
            


# In[ ]:


#pallimdrome


# In[98]:





# In[3]:


x=259 #python call by object refrence
#x 256 se uper jate hi cache memory me save nhi hota
print(id(x))
y=259
print(id(y))
x=20
print(id(x))
'''
if memory address change then immutable
memory address do not change the it is mutable


'''


# In[10]:


mydict.issuperset()


# In[9]:


mytuple=(10,20,30) #unpacking the tuple
x,y,z=mytuple
print(x,y,z)


# In[22]:


mydict={(1, 'yash'), (2, 'jaipur'), ('regex', 'deep')}
dict(mydict) # dict tuple to dict 


# In[21]:


mydict={1:'yash',2:"jaipur",'regex':"deep"}
x=mydict.items()
x


# In[29]:


myset1={1,2}
myset2={3,4,5,6,7}
myset1.isdisjoint(myset2)


# In[32]:


myset1={1,2,3,4}
myset2={3,4,1,2}
myset1.issuperset(myset2)


# In[37]:


myset1={1,2,3,4,5,6}
myset2={5,6,7,8}
myset2.difference(myset1)


# In[ ]:




