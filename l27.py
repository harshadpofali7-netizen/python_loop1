#program to print all factors of number
num = int(input("enter the number"))
print(f"The factor of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        