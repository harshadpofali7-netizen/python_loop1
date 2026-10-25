#program to print number until user enters a negative number
print("Enter numbers. Enter a negative number to stop:")
while True:
    num = float(input("Enter a number:"))
    if num < 0:
        print("Negative number detected:")
        break
    print(f"You entered:{num}")
    