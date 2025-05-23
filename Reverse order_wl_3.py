num = int(input("Enter a number: "))

original_num = num

if num < 0:
    num = -num

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num = num // 10 
        count += 1       

print(f"The number of digits in {original_num} is {count}.")