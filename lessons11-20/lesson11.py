'''
int()
str()
float()
bool True False
binary

1 = True
0 = False'''

import cs50
bool == True or False
number = cs50.get_int("Give me a number between 1 and 10.")
if number > 10:
    print("The number is more than 10.")
elif number < 1:
    print("The number is less than 1.")
elif number < 5:
    print("The number is less than five.")

elif number == 5:
    print("The number is 5.")
else:
    print("The number is more than five.")

