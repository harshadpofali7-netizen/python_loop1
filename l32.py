#program to calculate power of number without using pow()
base = float(input("Enter the base number:"))
exponent = int(input("Enter the exponent:"))
result = 1.0
abs_exponent = abs(exponent)
for _ in range(abs_exponent):
    result *= base
if exponent < 0:
    result =1 / result
print(f"{base} raised to the power of {exponent} is :{result}")
