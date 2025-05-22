char = input("Enter a single alphabet: ")

if len(char) == 1 and char.isalpha():
   
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")
else:
    print("Please enter only one alphabet (A-Z or a-z).")