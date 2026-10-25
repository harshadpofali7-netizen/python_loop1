#program to find largest digit
num = 39472
temp = abs(num)
largest_digit = 0
if temp > 0:
    largest_digit = 0
else:
    while temp > 0:
        last_digit = temp % 10
        if last_digit > largest_digit:
            largest_digit = last_digit
        temp = temp // 10
print(f"The largest digit in {num} is {largest_digit}")
