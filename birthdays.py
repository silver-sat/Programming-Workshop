"""Display birthdays from dictionary

From Exercise 33 in practicepython.org

"""

import datetime

# Store birthdays

birthdays = {
    "Albert Einstein": datetime.date(1879, 3, 14),
    "Benjamin Franklin": datetime.date(1706, 1, 17),
    "Ada Lovelace": datetime.date(1815, 12, 10)
    
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

print("That birthday is", birthdate.strftime("%A %B %d, %Y"))