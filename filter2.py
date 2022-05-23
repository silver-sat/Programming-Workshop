# Solutions to practicepython.org Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 81, 100]

# List comprehension

b = list(value for value in a if value % 2 == 0)

print("Using list comprehension:\n", b)
    



