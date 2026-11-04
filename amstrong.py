number = int(input("Enter a positive integer: "))

if number >= 0:
    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    if total == number:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


