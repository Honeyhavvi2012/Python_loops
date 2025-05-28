n1 = input("Enter the number of rows: ")
n = int(n1)

for i in range(n):
    for j in range(n - i - 1):  # Print spaces
        print(" ", end = "")
    for k in range(i + 1):  # Print stars
        print("*", end = "")
    print()
