# Common elements in two lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(item for item in a if item in b)
print(common_elements)
deduped_list = list()
for item in common_elements:
    if item not in deduped_list:
        deduped_list.append(item)
print(deduped_list)