# Solutions to practicepython.org Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 81, 100]

# Filter

def even(number):
    if number % 2 == 0:
        return True
    return False

b = list(filter(even, a))

print("Using filter():\n", b)