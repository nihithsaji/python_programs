numbers = input("Enter the numbers separated by spaces: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
largest = numbers[0]
smallest = numbers[0]

for item in numbers:
    if item > largest:
        largest = item
    if item < smallest:
        smallest = item

print("Largest:", largest)
print("Smallest:", smallest)

