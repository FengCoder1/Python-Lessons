import cs50


money = cs50.get_int("How much money do you have?")

use = cs50.get_int("How much money did you use?")

store = cs50.get_string("What store did you go to?")

print(f"You went to {store} and you have {money - use} left")

print(15 / 5)
print(2 + 1)


age = int(cs50.get_string("How old are you?"))
year = str(int(age) + 1)

print(f"Next year you will be {year} years old")