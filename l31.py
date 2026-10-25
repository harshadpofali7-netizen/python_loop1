#program to generate first n odd number
n = int(input("Enter how many odd number you want"))
count = 0
num = 1
print(f"The first {n} odd number are:")
while count < n:
    print(num, end="  ")
    num += 2
    count += 1
    