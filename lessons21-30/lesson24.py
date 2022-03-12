counter1 = 1
counter2 = 1
counter3 = 11
while counter1 < 11:
    while counter2 < counter3:
        print("# ", end="")
        counter2 += 1
    counter1 += 1
    counter2 = 1
    counter3 -= 1
    print()
