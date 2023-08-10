amount=int(input("enter the amount"))
notes=int(input("enter the notes which you take"))
num_notes=0
if(notes==10):
    num_notes=amount//10
    print("notes of 10 is",num_notes)
elif(notes==100):
    num_notes=amount//100
    print("notes of 100 is",num_notes)
elif(notes==500):
    num_notes=amount//500    
    print("notes of 500 is",num_notes)
else:
    print("notes is not available")    