# Remove duplicates from lists

# Create lists for testing

a = []

b = [1]

c = [2, 7, 3, 8, 6]

d = [2, 7, 2, 3, 3, 8, 8, 8, 6]

test_lists =[a, b, c, d]

# For each list, remove duplicates and print

for test_list in test_lists:
    new_set = set()
    for entry in test_list:
        new_set.add(entry)
    print(list(new_set))