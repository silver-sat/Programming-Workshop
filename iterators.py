# Iterator examples
#
print("A list: ")
for element in [1, 2, 3]:
    print(element)

print("\nA tuple: ")
for element in (1, 2, 3):
    print(element)

print("\nA dictionary: ")
for key in {'one':1, 'two':2}:
    print(key)

print("\nA string: ")
for char in "123":
    print(char)

print("\nA file: ")    
for line in open("myfile.txt"):
    print(line, end='')