#program to find sum of odd number
num = 24783
temp = abs(num)
odd_sum = 0
while temp > 0:
    last_digit = temp % 10
    if last_digit % 2 != 0:
        odd_sum += last_digit
    temp = temp // 10
print(f"The sum of odd digits in {num} is {odd_sum}")
