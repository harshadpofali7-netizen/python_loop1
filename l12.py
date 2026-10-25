#program to reverse a number
num = 12345
temp = abs(num)
reverse_num = 0
while temp > 0:
    last_digit = temp % 10
    reverse_num = (reverse_num * 10) + last_digit
    temp = temp // 10
if num < 0:
    reverse_num = -reverse_num
print(f"The raverse number is : {reverse_num}")
