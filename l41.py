#program to print number are perfect cubes 
print("Perfect cubes between 1 and 100 are:")
i = 1
while True:
    cube = i ** 3
    if cube > 100 :
        break
    print(cube, end="  ")
    i += 1
    