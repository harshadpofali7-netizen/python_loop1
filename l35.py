#program to print multiplication table from 1 to 5
for i in range(1, 6):
    print(f"---multiplication table of {i}---")
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()
    