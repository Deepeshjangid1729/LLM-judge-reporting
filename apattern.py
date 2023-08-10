# A pattern 
for i in range(0,5):
    for j in range(0,5):
        if(i==0 and (j!=0 and j!=4) or j==0 and i!=0 or j==4 and i!=0 or i==2):
            print("*",end="  ")
        else:
            print(end="   ")
    print("\n")            