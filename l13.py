#program to check a number is palindrome
num = 12321
if num < 0:
    is_palindrome = False
else:
    temp = num
    reversed_num = 0

    while temp > 0:
        last_digit = temp % 10
        reversed_num = (reversed_num * 10) + last_digit
        temp = temp // 10
    is_palindrome = (num == reversed_num)
if is_palindrome:
    print(f"{num} is a palindrome number .")
else:
    print(f"{num} is not a palindrome number")
    