# String formatting
#

data = [2.8, 3.5, 4.57, -1.0, 12.2]
width = 8
precision = 2
for index, value in enumerate(data):
    print(f'Result {index + 1}: {value:{width}.{precision}f}')