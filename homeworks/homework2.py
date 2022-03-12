counter = 5
answer = ""
shopping_list = []
while counter > 0:
    answer = input("What do you want to add to your shopping list?")
    shopping_list.append(answer)
    counter -= 1
print(shopping_list)
print(shopping_list[int(input("What item in the shopping list do you want to print?"))-1])