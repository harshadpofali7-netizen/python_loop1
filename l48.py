#program to check number is strong number
import math

def is_strong_number(num):
    digit_sum = sum(math.factorial(int(digit)) for digit in str(num))
    return digit_sum == num

test_num = 145
if is_strong_number(test_num):
    print(f"{test_num} is a strong number")
else:
    print(f"{test_num} is not a strong number")
    