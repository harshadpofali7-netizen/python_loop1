#program to find smallest digit in a number
num_input = input("Enter a number:")
digits = [char for char in num_input if char.isdigit()]
if digits:
    smallest_digit = min(digits)
    print(f"The smallest digit in the number is: {smallest_digit}")
else:
    print("No valid digits were entered:")
    