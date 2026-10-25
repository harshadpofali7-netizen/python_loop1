#program to print fibonacci series ut to n terms
n_terms = 10
n1, n2 = 0, 1
count = 0
if n_terms <= 0:
    print("Please enter a pofitive integer.")
elif n_terms == 1:
    print(f"Fibonacci sequence up to {n_terms} term:")
    print(n1)
else:
    print(f"Fibonacci sequence up to {n_terms} term:")
    for _ in range(n_terms):
        print(n1, end="  ")
        
        nth = n1 + n2
        n1 = n2
        n2 = nth
