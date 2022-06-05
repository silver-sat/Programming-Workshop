# Exercise 38 from practicepython.org
#

from datetime import date
today = date.today()

# Get user name and age

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
if user_age.isnumeric():
    user_age = int(user_age)
else:
    print("That is not a valid age")
    quit()
    
# Print the result
    
print(f'{user_name}, you will be 100 years old in {today.year + 100 - user_age}')