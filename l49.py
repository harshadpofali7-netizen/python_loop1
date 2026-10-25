#program to display menu-driven using while loop
import math
def product_of_digits(num):
    num = abs(num)
    if num == 0:
        return 0
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product
def is_strong_number(num):
    if num <= 0:
        return False
    digit_sum = sum(math.factorial(int(digit)) for digit in str(num))
    return digit_sum == num

while True:
    print("\n" + "="*30)
    print("     MAIN MENU     ")
    print("="*30)
    print("1. Find product of digits")
    print("2. Check for strong number")
    print("3. Exit")
    print("="*30)

    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        try:
            n = int(input("Enter an integer:"))
            print(f"The product of the digits of {n} is: {product_of_digits(n)}")
        except ValueError:
            print("Invalid input! Please enter a valid integer")
    elif choice == "2":
        try:
            int(input("Enter a positive integer: "))
            if is_strong_number(n):
                print(f"Yes, {n} is a strong number!")
            else:
                print(f"No, {n} is not a strong number")
        except ValueError:
            print("Invalid input! Please enter a valid integer")
    elif choice == "3":
        print("\nThank you for using the program. Goodbye")
        break
    else:
        print("Inavlid choice! Please select an option between 1 and 3.")
        