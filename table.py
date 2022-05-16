# Format tabluar data

# Print the header

print(f"{'Value':^8}", f"{'Square':^8}", f"{'Cube':^8}")

# Generate the data and print the table

for index in range(1, 11):
    print(f"{index:>8}", f"{index**2:>8}", f"{index**3:>8}")