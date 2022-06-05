# Display birthdays from dictionary
#

from datetime import date

# Store birthdays

birthdays = {
    "Albert Einstein": date(1879, 3, 14),
    "Benjamin Franklin": date(1706, 1, 17),
    "Ada Lovelace": date(1815, 12, 10)
    
    }

# Print the birthdays we know

print("I know the following birthdays:")

for name in birthdays.keys():
    print(name) 

# Ask for the name to look up

while True:
    try:
        entry = input("Enter the name ('!' to quit): ")
        if entry == '!':
            quit()
        birthdate = birthdays[entry]
        break
    except KeyError:
        print("That was not a valid name. Try again...")

# Print the name and the birthday

print(f'That birthday is {birthdate:%A %B %d, %Y}')