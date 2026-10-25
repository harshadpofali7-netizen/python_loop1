#program to count no. of digits in anumber
num =12345
temp = abs(num)
count = 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp = temp // 10
print(f"The number of digits in {num} is {count}")
