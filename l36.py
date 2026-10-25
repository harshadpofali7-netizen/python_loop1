#program to find sum of number entered until 0 is enter
total_sum = 0
print("Enter numbers to sum up.")
while True:
    num = float(input("Enter a number:"))
    if num == 0:
        break
    total_sum += num
print(f"\nThe loop has ended. the total sum of your number is :{total_sum}")
