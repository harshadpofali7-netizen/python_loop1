#program to find product of digits of a number
def product_of_digits(num):
    num = abs(num) 
    product = 1

    if num == 0:
        return 0

    while num > 0:
        product *= num % 10
        num //= 10

    return product
print(product_of_digits(47))
