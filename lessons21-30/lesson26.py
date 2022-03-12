counter1 = 1
counter2 = 1
lines = int(input("How many lines do you want the triangle to have?")) + 1
counter3 = lines
counter4 = 1
while counter1 < lines:
    while counter4 < counter1:
        print("  ", end="")
        counter4 += 1
    while counter2 < counter3:
        print("# ", end="")
        counter2 += 1
    counter1 += 1
    counter2 = 1
    counter3 -= 1
    counter4 = 1
    print()