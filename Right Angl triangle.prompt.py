n1 = input("Enter the number of rows:")
n = int(n1)
for i in range(n):
    for j in range(i+1):
        print("*", end = "")
    print()