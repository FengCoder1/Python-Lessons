import cs50

number = cs50.get_int("Give me a number between 10 and 20")
if number > 10 and number < 20:
    print("The number is between 10 and 20")
else:
    print("The number is not between 10 and 20")
if number <= 10 or number >= 20:
    print("The number is not between 10 and 20")
else:
    print("The number is between 10 and 20")

age = cs50.get_string("Are you older than 10 years old?")
if age.upper() == "YES":
    print("You are older than 10")
else:
    print("You're not older than 10")
print(age.capitalize())