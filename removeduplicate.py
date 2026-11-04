numbers = input("Enter the numbers separated by spaces: ").split()

new_list = []

for number in numbers:
    num = int(number)
    if num not in new_list:
        new_list.append(num)

print(new_list)

