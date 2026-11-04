text=input("Enter a string : ")
counts={}
for char in text:
  counts[char]=counts.get(char,0)+1
for char,count in counts.items():
  print(char,":",count)
