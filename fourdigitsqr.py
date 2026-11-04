start=int(input("Enter the start of the range : "))
end=int(input("Enter the end of the range : "))
results=[]
for root in range(32,100):
  number=root*root
  if start<=number<=end:
    if all(int(digit)%2==0 for digit in str(number)):
       results.append(number)
print(results)
