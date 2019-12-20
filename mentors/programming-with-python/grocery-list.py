grocery_list_items = 'lettuce tomatoes berries carrots oats milk yoghurt eggs'

grocery_list = grocery_list_items.split()

print(grocery_list)

print(grocery_list[0])

print(grocery_list[5])

print(grocery_list.pop(3))

print(grocery_list[-3:])


for item in grocery_list:
    print(item)