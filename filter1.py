# Solutions to practicepython.org Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 81, 100]

# For loop

b = list()
for index in range(len(a)):
    value = a[index]
    if (value % 2 == 0):
        b.append(value)
             
print("Using for loop:\n", b)