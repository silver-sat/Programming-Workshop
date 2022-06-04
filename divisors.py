# Print the divisors of a number

# Get the number

number = int(input("Please enter a number: "))

# For everything less than the number, see if it divides evenly

divisors = list()
for test_number in range(1, number + 1):
    if (number % test_number == 0):
        divisors.append(test_number)
print(divisors)