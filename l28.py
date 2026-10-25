#program to check the number is armstrong
num = int(input("Enter a number:"))
num_str = str(num)
num_digit = len(num_str)
digit_sum = 0
for digit in num_str:
    digit_sum += int(digit) ** num_digit
if digit_sum == num:
    print(f"{num} is an armstrong number")
else:
     print(f"{num} is not an armstrong number")
     