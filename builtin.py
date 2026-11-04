s=input("Enter a string: ")
a=int(input("enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

print("\nLength of string: ",len(s))

print("Maximum number: ",max(a,b,c))
print("Minimum number: ",min(a,b,c))

numbers=[a,b,c]
print("Sorted list: ",sorted(numbers))

print("sum of numbers: ",sum(numbers))

print("Uppercase string ",s.upper())

print("Absolute value of first number: ",abs(a))

print("power: ",pow(a,b))

print("Reversed list : ",list(reversed(numbers)))

print("Type of string: ",type(s))
print("Type of integer: ", type(a))
