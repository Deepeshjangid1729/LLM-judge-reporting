actual_pass="Mohit@123"
password=input("enter the pssword:\n charctor\n number\n symbol\n")
if len(password)>=8:
    for i in range(len(actual_pass)):
        if(actual_pass[i::]==password[::]):
           print("password is right")
           break
        else:
            print("password is wrong")  
            break 
else:
    print("password is weak please try again::")        
            