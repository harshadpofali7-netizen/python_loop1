#program to calculate sum of cubes 
n = int(input("Enter the value of n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i ** 3
print(f"The sum of cubes of the {n} is :{total_sum}")

