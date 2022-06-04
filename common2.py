# Identify common elements from lists with sets

# Create lists for testing

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Identify common elements and print

print (list(set(a) & set(b)))
