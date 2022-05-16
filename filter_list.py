# Solutions to practicepython.org Exercise 7

a = [1, 4, 9, 16, 25, 36, 49, 81, 100]

# For loop

b =[]
for index in range(len(a)):
    if (a[index] % 2 == 0):
        b.append(a[index])
             
print("Using for loop:\n", b)

# List comprehension

b = list(number for number in a if number % 2 == 0)

print("Using list comprehension:\n", b)

# Filter

def even(number):
    if number % 2 == 0:
        return True
    return False

b = list(filter(even, a))

print("Using filter():\n", b)


# Filter

b = list(filter(lambda item: item % 2 == 0, a))

print("Using filter() with lambda:\n", b)
    



