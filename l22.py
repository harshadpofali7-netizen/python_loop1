#program to find sum of even digit in a number
num = 24783
temp = abs(num)
even_sum = 0
while temp > 0:
    last_digit = temp % 10
    if last_digit % 2 == 0:
        even_sum += last_digit
    temp = temp // 10
print(f"The sum of even digits in {num} is {even_sum}")
