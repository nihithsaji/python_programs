limit=int(input("Enter the limit"))
for row in range(1,limit+1):
  for colum in range(1,row+1):
    print("*",end=" ")
  print()
for row in range(limit-1,0,-1):
  for colum in range(1,row+1):
    print("*",end=" ")
  print()
   
   
   
   
   
   
   
   
   
   
   

