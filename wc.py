# Simple wc in Python
#

from sys import exit

# Counters

file_lines = 0
file_words = 0
file_bytes = 0

# Get file name

file_name = input("Enter file name: ")

# Read and count

try:
    with open(file_name, 'r') as open_file:
        for line in open_file:
            file_lines += 1
            file_words += len(line.split())
            file_bytes += len(line)
except OSError as error:
    print(f'Opening file {file_name} failed due to: {error}')
    exit(1)

# Print results

print(f'{file_lines:8}', end = '')
print(f'{file_words:8}', end = '')
print(f'{file_bytes:8}', end = '')