#program to print first nmultiples of a number
num = 5
n = 6
for i in range(num, (num * n) + n, num):
    print(i, end=" ")
    