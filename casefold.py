# Use case folding and isnumeric to check user input
#

# Get user input

user_entry = input("Please enter a number or 'Q' to quit: ")

if user_entry.casefold() == 'q':
    print('Exiting')
    quit()
else:
    if user_entry.isnumeric():
        number = int(user_entry)
        print(number)
    else:
        print("Entry is not a number")

    

