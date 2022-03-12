things = ["get up", "get dressed", "have breakfast", "brush my teeth", "study online"]

# Change 1s into 0s
counter1 = 0
counter2 = 0
lines = int(input("How many lines do you want the triangle to have?")) +1
counter3 = lines
counter4 = 0
while counter1 < lines:
    while counter4 < counter1:
        print("  ", end="")
        counter4 += 1
    while counter2 < counter3:
        print("# ", end="")
        counter2 += 1
    counter1 += 1
    counter2 = 0
    counter3 -= 1
    counter4 = 0
    print()