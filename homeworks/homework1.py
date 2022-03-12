import cs50

print("Hello. My name is Feng.")
player_name = cs50.get_string("What's yours?")
print(f"Hello, {player_name}. Nice to meet you.")

friend = cs50.get_string("Who's your best friend forever?")
if friend == "Feng" or friend == "Ingfa" or friend == "you" or friend == "Ingfa Tanalekhapat":
    print(f"Thanks, {player_name}. We can be good friends.")
elif friend == "no one":
    print("Me too! I have 2 best friends Namaoony and Rinny.")
else:
    print(f"Oh, {friend} must be so nice to you.")

age = cs50.get_int("How old are you?")
if age > 10:
    print("You're older than me. I'm only 10.")
elif age < 10:
    print("You're younger than me. I'm ten :)")
elif age == 10:
    print("Yay, we're the same age!")

do_in_the_morning = cs50.get_string("What do you do first in the morning?")
print("First, I brush my teeth.")

money = cs50.get_int("How much money do you have today?")
if money > 100:
    print("Woah, you get a lot of money!")
else:
    print("Okay.")

used_money = cs50.get_int("How much money did you use?")
print(f"So, you have {money - used_money} left.")

how_are_you = cs50.get_string("How are you today? (Good or Bad)")
if how_are_you.lower() == "good":
    print("That's great! I'm good, too.")
elif how_are_you.lower() == "bad":
    print("Oh, I am so sorry for you.")

print("Bye!")