#program to find sum of digits of a number 
num = 12345
temp = abs(num)
digit_sum = 0
while temp > 0:
    last_digit = temp % 10
    digit_sum += last_digit
    temp = temp // 10
print(f"The sum of the digits of {num} is {digit_sum}")
