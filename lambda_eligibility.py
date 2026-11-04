age=int(input("Enter your age : "))
eligibile = lambda age: "eligible" if age >= 18 else "not eligible"
print(eligibile(age))
