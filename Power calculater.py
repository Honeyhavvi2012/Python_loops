base = int(input("Enter the base number: "))
n = int(input("Enter how many powers to calculate: "))

print(f"Calculating powers of {base} from 1 to {n}:")

# Calculating and displaying the powers directly
for i in range(1, n + 1):
    result = base ** i
    print(f"{base}^{i} = {result}")