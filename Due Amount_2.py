def calculate_change(amount_paid, total_bill):
    return amount_paid - total_bill

change_to_return = calculate_change(4.00, 2.50)
print("The shopkeeper should return $", change_to_return)
