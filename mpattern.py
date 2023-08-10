'''
  0 1 2 3 4 
0 * * * * * 
1     *    
2     *    
3 *   *   
4 * * *       
'''
'''
# M pattern 
for i in range(0,5):
    for j in range(0,5):
        if(j==0 or  j==4 or i-j==0 and i<=2 or j-i==2 and i!=0 ):
            print("*",end=" ")
        else:
            print(end="  ") 
    print("\n")           
  '''
 # D pattern
'''
for i in range(0,5):
    for j in range(0,5):
         if(j==0 or i==0 and j!=4 or i==4 and j!=4 or j==4 and (i!=0 and i!=4)  ):
             print("*",end=" ")
         else:
             print(end="  ")  
    print("\n")                
'''
# J pattern
for i in range(0,5):
    for j in range(0,5):
        if(i==0 or j==2 or i==4 and(j!=3 or j!=4) or j==0 and (i!=1 or i!=2) ):
            print("*",end=" ")
        else:
            print(end="  ")
    print("\n")
    