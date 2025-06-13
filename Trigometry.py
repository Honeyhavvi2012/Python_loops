import math

def simple_math_tool():
    try:
        num = float(input("Enter a number: "))

        if math.isnan(num):
            print("You entered NaN! Try again.")
            return
        
        if num >= 0 and num.is_integer():
            print(f"Factorial of {int(num)} is {math.factorial(int(num))}")
        else:
            print("Factorial is not defined for negative or decimal numbers.")

        print(f"e^{num} is {math.exp(num)}")
        
        print(f"{num} radians is {math.degrees(num)} degrees")

    except ValueError:
        print("Invalid input! Please enter a number.")

simple_math_tool()
