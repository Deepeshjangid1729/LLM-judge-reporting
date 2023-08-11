lst=["deepesh","anil","sunil"]

input_your_name=input("enter the your name")
while(1):
   number=int(input("enter the number 1. check your name\n 2.insert your name \n 3.delete your name\n"))
   if(number==1):
       for i in range(len(lst)):
           if(lst[i]==input_your_name):
               print("your name is present in list ")
               break
           else:
              print("your name is not in list please add the name and press 2")  
              break
                 
   elif(number==2):
        name=input("please enter the your name")
        lst.append(name)
        print("your name is add in list please check it and press 1")
   elif(number==3):
        lst.remove(input_your_name)
        print("your name is delete from list")            
   else:
        print("enter the corrent number only press 1 2 3 ")   
        
        
                
        
        