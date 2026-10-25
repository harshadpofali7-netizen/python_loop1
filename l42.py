#program to calculate sum of square 
n = int(input("Enter the value of n:"))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i ** 2
print(f"The sum of square of the first {n} number is:{total_sum}")
