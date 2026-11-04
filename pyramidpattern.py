limit = int(input("Enter the limit: "))

for row in range(1, limit + 1):
    for space in range(1, limit - row + 1):
        print(" ", end="")

    for column in range(1, 2 * row):
        print("*", end="")

    print()
