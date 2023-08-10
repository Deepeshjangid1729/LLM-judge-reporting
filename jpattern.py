# j pattern 
for i in range(0,5):
    for j in range(0,5):
          if(i==0 or j==2 or i==4 and (j!=4 and j!=3)  or j==0 and (i!=1 and i!=2 )):
              print("*",end=" ")
          else:
              print(end="  ")    
    print("\n")      
          