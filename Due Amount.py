bills = [2.50, 4.00]
paid_amounts = [4.00, 4.00]

for i in range(len(bills)):
    if paid_amounts[i] == bills[i]:
        continue  
    change = paid_amounts[i] - bills[i]
    print("Return $", change)