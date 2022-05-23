# Print the divisors of a number

# Get the number

number = int(input("Please enter a number: "))

# For everything less than the number, see if it divides evenly

for test_number in range(1, number):
    if (number % test_number == 0):

# If so, print the number

        print(test_number, " is a divisor")