# Create list with common elements

# Lists for test

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list()
for item in a:
    if item in b:
        common_elements.append(item)
print(common_elements)
    