input_function = input("Does input function work?")

print(input_function.lower())

if input_function.lower() == "yes":
    print("The input function works.")
elif input_function.lower() == "no":
    print("The input function does not work.")